import argparse
import subprocess

def svn_commit(directory, message):
    cmd = "svn commit -m '{}' {}".format(message, directory)
    subprocess.run(cmd, shell=True, check=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Execute svn commit in a specific directory")
    parser.add_argument("directory", type=str, help="The directory to perform the commit")
    parser.add_argument("message", type=str, help="The commit message")
    args = parser.parse_args()
    
    svn_commit(args.directory, args.message)
