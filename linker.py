import os
import shutil
import subprocess

def replace_changed_objects(recom_dir="__recom__", history_dir="__history__"):
    
    if not os.path.exists(recom_dir):
        print(f"No directory named '{recom_dir}'. Skipping replacement.")
        return

    if not os.path.exists(history_dir):
        os.makedirs(history_dir)

    replaced = []
    for file in os.listdir(recom_dir):
        if file.endswith(".o"):
            src = os.path.join(recom_dir, file)
            dst = os.path.join(history_dir, file)
            shutil.copyfile(src, dst)
            replaced.append(file)
            print(f"Replaced {dst} with new version from {src}")
    return replaced

def link_all_objects(history_dir="__history__", output_binary="final.out") -> bool:
    
    object_files = [os.path.join(history_dir, f) for f in os.listdir(history_dir) if f.endswith(".o")]

    if not object_files:
        print("No object files found to link.")
        return False

    result = subprocess.run(["gcc", *object_files, "-o", output_binary])
    
    if result.returncode == 0:
        print(f"Successfully linked → {output_binary}")
        return True
    else:
        print("Linking failed.")
        return False

# CLI usage
if __name__ == "__main__":
    print("Running linker.py (CLI mode)...")
    replace_changed_objects()
    link_all_objects()