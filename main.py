import os
import shutil

# Define paths
data_dir = r"C:\xampp\mysql\data"
backup_dir = r"C:\xampp\mysql\backup"

# Folders to delete in data_dir
folders_to_delete = ["phpmyadmin", "performance_schema", "mysql", "test"]

# File to exclude from deletion in data_dir
file_to_exclude = "ibdata1"


def delete_specific_folders(directory, folders):
    """Delete specific folders in the given directory."""
    for folder in folders:
        folder_path = os.path.join(directory, folder)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            print(f"Deleting folder: {folder_path}")
            shutil.rmtree(folder_path)


def delete_files_except(directory, exclude_file):
    """Delete all files in the directory except the specified file."""
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path) and item != exclude_file:
            print(f"Deleting file: {item_path}")
            os.remove(item_path)


def copy_files_except(source, destination, exclude_file):
    """Copy all files and folders from source to destination, excluding the specified file."""
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        # Skip the excluded file
        if item == exclude_file:
            print(f"Skipping file: {item}")
            continue

        if os.path.isdir(source_path):
            print(f"Copying folder: {source_path} -> {destination_path}")
            shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
        elif os.path.isfile(source_path):
            print(f"Copying file: {source_path} -> {destination_path}")
            shutil.copy2(source_path, destination_path)


def main():
    print("Starting cleanup and restoration process...")

    # Step 1: Delete specific folders in data_dir
    delete_specific_folders(data_dir, folders_to_delete)

    # Step 2: Delete all files in data_dir except ibdata1
    delete_files_except(data_dir, file_to_exclude)

    # Step 3: Copy files and folders from backup_dir to data_dir, excluding ibdata1
    copy_files_except(backup_dir, data_dir, file_to_exclude)

    print("Process completed successfully.")
    print("Restart XAMPP.")

if __name__ == "__main__":
    main()