import argparse
import os
import shutil

def move_files(src_dir, dst_dir, search_string=None):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if not search_string or search_string in file:
                src_file = os.path.join(root, file)
                dst_file = src_file.replace(src_dir, dst_dir, 1)
                dst_dir_path = os.path.dirname(dst_file)
                if not os.path.exists(dst_dir_path):
                    os.makedirs(dst_dir_path)
                shutil.move(src_file, dst_file)
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
    move_files(args.src_dir, args.dst_dir, args.search_string)
