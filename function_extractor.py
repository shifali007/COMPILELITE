import os
import re
import sys

def extract_functions_from_file(file: str, functions: list[str], output_dir="__obj__"):
    
    with open(file, "r") as f:
        lines = f.readlines()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    extracted = {}
    inside_function = False
    current_func = ""
    brace_count = 0
    header_lines = []

    # all lines before the first function as header (includes)
    for i, line in enumerate(lines):
        if re.match(r"\w[\w\s\*]*\s+\w+\s*\([^;]*\)\s*\{", line):
            header_lines = lines[:i]
            break

    for i, line in enumerate(lines):
        # Match function signature
        match = re.match(r"(\w[\w\s\*\[\]]*?)\s+(\w+)\s*\([^;]*\)\s*\{", line.strip())
        if match:
            current_func = match.group(2)
            if current_func in functions:
                inside_function = True
                brace_count = 1
                extracted[current_func] = header_lines[:] + [line]
                continue

        elif inside_function:
            extracted[current_func].append(line)
            brace_count += line.count("{")
            brace_count -= line.count("}")
            if brace_count == 0:
                inside_function = False
                current_func = ""

    # Write each extracted function
    for func_name, func_lines in extracted.items():
        out_path = os.path.join(output_dir, f"{func_name}.c")
        with open(out_path, "w") as out_file:
            out_file.writelines(func_lines)
        print(f"Extracted {func_name} → {out_path}")

    return list(extracted.keys())

def read_changed_functions_from_txt(path="changed_functions.txt"):
    funcs = []
    files = set()
    with open(path, "r") as f:
        for line in f:
            match = re.match(r"(\w+)\s+\((.+?)\)", line.strip())
            if match:
                funcs.append(match.group(1))
                files.add(match.group(2))
    return list(files), funcs

# CLI usage
if __name__ == "__main__":
    print("Running function_extractor.py (CLI mode)")

    if not os.path.exists("changed_functions.txt"):
        print("changed_functions.txt not found.")
        sys.exit(1)

    files, functions = read_changed_functions_from_txt()
    for file in files:
        extracted = extract_functions_from_file(file, functions)
    print("Extraction complete.")
