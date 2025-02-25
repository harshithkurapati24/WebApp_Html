import os

# Specify the directory path
directory_path = '.'

# Loop through files and rename
for filename in os.listdir(directory_path):
    if filename.endswith(".jsp"):
        old_filename = os.path.join(directory_path, filename)
        new_filename = os.path.join(directory_path, filename.replace(".jsp", ".html"))
        os.rename(old_filename, new_filename)
        print(f"Renamed {filename} to {filename.replace('.jsp', '.html')}")
