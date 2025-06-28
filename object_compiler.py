import os
import re
import subprocess
import tempfile
from typing import List
import sys

def get_function_map(file: str) -> List[tuple[str, int]]:
    
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

def extract_function_code(file: str, func_name: str, start_line: int, end_line: int) -> List[str]:
    
    with open(file, "r") as f:
        lines = f.readlines()
    
    header_lines = []
    for i, line in enumerate(lines):
        if re.match(r"\w[\w\s\*]*\s+\w+\s*\([^;]*\)\s*\{", line):
            header_lines = lines[:i]
            break

    return header_lines + lines[start_line-1:end_line]

def compile_function_to_object(code_lines: List[str], func_name: str, output_dir: str = "__history__") -> bool:
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".c", delete=False) as tmp:
        tmp.writelines(code_lines)
        tmp_path = tmp.name

    output_path = os.path.join(output_dir, func_name + ".o")
    result = subprocess.run(["gcc", "-w", "-c", tmp_path, "-o", output_path])
    os.remove(tmp_path)

    if result.returncode == 0:
        print(f"Compiled {func_name} → {output_path}")
        return True
    else:
        print(f"Failed to compile {func_name}")
        return False

def build_object_history_from_file(source_file: str = "test.c", output_dir: str = "__history__") -> List[str]:
    
    func_map = get_function_map(source_file)
    compiled = []

    for i in range(len(func_map)):
        name, start = func_map[i]
        end = func_map[i+1][1] - 1 if i + 1 < len(func_map) else None
        code_lines = extract_function_code(source_file, name, start, end)
        if compile_function_to_object(code_lines, name, output_dir):
            compiled.append(name)
    
    return compiled

def link_objects(history_dir: str = "__history__", output_binary: str = "final.out") -> bool:
    object_files = [os.path.join(history_dir, f) for f in os.listdir(history_dir) if f.endswith(".o")]
    if not object_files:
        print("No object files found to link.")
        return False
    result = subprocess.run(["gcc", *object_files, "-o", output_binary])
    if result.returncode == 0:
        print(f"Linked → {output_binary}")
        return True
    else:
        print("Linking failed.")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    print("Building full function object cache into __history__...")
    compiled = build_object_history_from_file(filename)
    if compiled:
        print("Compiled", len(compiled), "functions.")
        link_objects()
    else:
        print("No functions compiled.")
