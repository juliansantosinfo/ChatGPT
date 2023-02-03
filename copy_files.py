import argparse
import os
import shutil

def copy_files(src_dir, dst_dir, search_string=None):
    if not os.path.exists(src_dir):
        print(f"Error: Source directory {src_dir} does not exist.")
        return
    if not os.path.exists(dst_dir):
        print(f"Error: Destination directory {dst_dir} does not exist.")
        return
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if not search_string or search_string in file:
                src_file = os.path.join(root, file)
                dst_file = src_file.replace(src_dir, dst_dir, 1)
                dst_dir_path = os.path.dirname(dst_file)
                if not os.path.exists(dst_dir_path):
                    os.makedirs(dst_dir_path)
                if os.path.exists(dst_file):
                    print(f"File {dst_file} already exists, skipped.")
                else:
                    shutil.copy2(src_file, dst_file)
                    print(f"Copied {src_file} to {dst_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Copy files to a destination directory')
    parser.add_argument('src_dir', nargs='?', type=str, help='Source directory')
    parser.add_argument('dst_dir', nargs='?', type=str, help='Destination directory')
    parser.add_argument('search_string', nargs='?', type=str, help='Search string (optional)')
    args = parser.parse_args()
    if not args.src_dir:
        args.src_dir = input("Enter source directory: ")
    if not args.dst_dir:
        args.dst_dir = input("Enter destination directory: ")
    copy_files(args.src_dir, args.dst_dir, args.search_string)
