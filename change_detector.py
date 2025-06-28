import subprocess
import re
import sys

def get_changed_files() -> list[str]:
    result = subprocess.run(["git", "diff", "--name-only"], capture_output=True, text=True)
    return [f.strip() for f in result.stdout.splitlines() if f.endswith(".c")]

def get_changed_lines(file: str) -> list[int]:
    result = subprocess.run(["git", "diff", "--unified=0", file], capture_output=True, text=True)
    changed_lines = []
    current_line = 0
    in_hunk = False

    for line in result.stdout.splitlines():
        if line.startswith("@@"):
            match = re.match(r"@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@", line)
            if match:
                current_line = int(match.group(1))
                in_hunk = True
        elif in_hunk:
            if line.startswith("+") and not line.startswith("+++"):
                changed_lines.append(current_line)
                current_line += 1
            elif line.startswith("-") and not line.startswith("---"):
                changed_lines.append(current_line)
            elif not line.startswith("-"):
                current_line += 1

    return sorted(set(changed_lines))

def get_function_map(file: str) -> list[tuple[str, int]]:
    result = subprocess.run(["ctags", "-x", "--c-kinds=f", file], capture_output=True, text=True)
    function_map = []
    for line in result.stdout.splitlines():
        parts = line.split()
        if len(parts) >= 3:
            name = parts[0]
            line_no = int(parts[2])
            function_map.append((name, line_no))
    function_map.sort(key=lambda x: x[1])
    return function_map

def find_function_for_line(line: int, func_map: list[tuple[str, int]]) -> str | None:
    for i in range(len(func_map)):
        name, start = func_map[i]
        end = func_map[i + 1][1] - 1 if i + 1 < len(func_map) else float('inf')
        if start <= line <= end:
            return name
    return None

def get_changed_functions(file: str) -> list[str]:
    changed_lines = get_changed_lines(file)
    func_map = get_function_map(file)
    changed_funcs = set()

    for line in changed_lines:
        func = find_function_for_line(line, func_map)
        if func:
            changed_funcs.add(func)

    return sorted(changed_funcs)

def commit_tracked_changes(files: list[str], message: str = "Changes tracked"):
    if not files:
        print("No .c files to commit.")
        return

    print("Committing:", files)
    subprocess.run(["git", "add"] + files)
    subprocess.run(["git", "commit", "-m", message])
    print("Changes committed.")

# CLI usage
if __name__ == "__main__":
    print("Detecting changes...")
    all_changed_funcs = []
    
    if len(sys.argv) == 2:
        target_file = sys.argv[1]
        changed_files = [target_file] if target_file.endswith(".c") else []
    else:
        changed_files = get_changed_files()

    for file in changed_files:
        funcs = get_changed_functions(file)
        if funcs:
            print(f"Changed functions in {file}:")
            for f in funcs:
                print(f"  - {f}")
                all_changed_funcs.append((file, f))

    with open("changed_functions.txt", "w") as out:
        for file, func in all_changed_funcs:
            out.write(f"{func} ({file})\n")

    if all_changed_funcs:
        commit_msg = "Tracked changes to: " + ", ".join(func for _, func in all_changed_funcs)
        commit_tracked_changes(changed_files, commit_msg)
    else:
        print("No function-level changes detected.")
