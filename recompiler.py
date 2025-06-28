import os
import subprocess
import sys

def compile_to_object(c_file: str, output_dir: str = "__recom__") -> str | None:
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    base_name = os.path.splitext(os.path.basename(c_file))[0]
    output_path = os.path.join(output_dir, base_name + ".o")

    result = subprocess.run(["gcc", "-w", "-c", c_file, "-o", output_path])

    if result.returncode == 0:
        print(f"Compiled {c_file} → {output_path}")
        return output_path
    else:
        print(f"Failed to compile {c_file}")
        return None

def recompile_all(obj_dir: str = "__obj__", out_dir: str = "__recom__") -> list[str]:
    
    compiled_objects = []
    if not os.path.exists(obj_dir):
        print(f"Object directory '{obj_dir}' not found.")
        return compiled_objects

    for filename in os.listdir(obj_dir):
        if filename.endswith(".c"):
            c_file = os.path.join(obj_dir, filename)
            obj_file = compile_to_object(c_file, out_dir)
            if obj_file:
                compiled_objects.append(obj_file)

    return compiled_objects

# CLI usage
if __name__ == "__main__":
    print("Running recompiler.py (CLI mode)")
    compiled = recompile_all()
    if compiled:
        print("Recompilation complete.")
    else:
        print("No files compiled.")
