import os
import shutil
import argparse

def copy_files_recursive(source_dir, target_dir):
    """
    Recursively copies and sorts files from the source directory into the target directory.
    Each file is copied to a subdirectory named after its extension.
    
    Parameters:
        source_dir (str): Path to the source directory.
        target_dir (str): Path to the target directory.
    """
    try:
        # Ensure target directory exists
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        # Iterate through all elements in the source directory
        for entry in os.listdir(source_dir):
            source_path = os.path.join(source_dir, entry)  # Full path of the current entry

            try:
                # If entry is a file, handle copying
                if os.path.isfile(source_path):
                    # Extract file extension and handle files with no extension
                    file_extension = os.path.splitext(entry)[1].lower()
                    if not file_extension:  # If no extension, use "no_extension"
                        file_extension = "no_extension"

                    # Create subdirectory in the target directory based on file extension
                    extension_dir = os.path.join(target_dir, file_extension[1:] if file_extension != "no_extension" else file_extension)
                    if not os.path.exists(extension_dir):
                        os.makedirs(extension_dir)

                    # Copy the file to the appropriate subdirectory
                    target_path = os.path.join(extension_dir, entry)
                    shutil.copy2(source_path, target_path)  # Copy file with metadata
                    print(f"Copied: {source_path} -> {target_path}")

                # If entry is a directory, call the function recursively
                elif os.path.isdir(source_path):
                    print(f"Entering directory: {source_path}")
                    copy_files_recursive(source_path, target_dir)

            except PermissionError:
                print(f"Permission denied: {source_path}")
            except shutil.Error as e:
                print(f"Error copying file '{source_path}': {e}")
            except Exception as e:
                print(f"Unexpected error with file '{source_path}': {e}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    Main function to parse arguments or interactively ask for directories.
    """
    parser = argparse.ArgumentParser(description="Recursively copy files and sort them by extensions.")
    parser.add_argument("source", nargs="?", help="Path to the source directory")
    parser.add_argument("destination", nargs="?", help="Path to the destination directory (default: 'dist')")

    args = parser.parse_args()

    # Check if source directory is provided
    if not args.source:
        print("Arguments not provided. Switching to interactive mode.")
        source_dir = input("Enter the path to the source directory: ").strip()
        target_dir = input("Enter the path to the target directory (default: 'dist'): ").strip()

        if not target_dir:
            target_dir = "dist"
    else:
        source_dir = args.source
        target_dir = args.destination if args.destination else "dist"

    # check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    print(f"Copying files from '{source_dir}' to '{target_dir}'...")
    copy_files_recursive(source_dir, target_dir)
    print("File copying and sorting completed!")


if __name__ == "__main__":
    main()
