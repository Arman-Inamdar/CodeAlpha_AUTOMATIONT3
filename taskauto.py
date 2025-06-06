
import os
import shutil

# Source and Destination folders
source_folder = r'D:\TASKAUTOMATION\FOLDER1'      
destination_folder = r'D:\TASKAUTOMATION\FOLDER2' 


if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through files in source
for filename in os.listdir(source_folder):
    if filename.lower().endswith('.jpg'):
        src_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(destination_folder, filename)
        
        shutil.move(src_path, dest_path)
        print(f"Moved: {filename}")

print(" All .jpg files moved successfully.")
