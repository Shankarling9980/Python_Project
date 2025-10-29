import os
import shutil

# Folders (you can change these paths)
source = "source_folder"
destination = "destination_folder"

# Create folders if not exist
os.makedirs(source, exist_ok=True)
os.makedirs(destination, exist_ok=True)

# Move .jpg files
for file in os.listdir(source):
    if file.endswith(".jpg"):
        shutil.move(os.path.join(source, file), os.path.join(destination, file))
        print(f"Moved: {file}")

print("\n✅ All JPG files moved successfully!")