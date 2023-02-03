import argparse
import subprocess

def git_commit(directory, message):
    cmd = "cd {} && git commit -am '{}'".format(directory, message)
    subprocess.run(cmd, shell=True, check=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Execute git commit in a specific repository")
    parser.add_argument("directory", type=str, help="The repository to perform the commit")
    parser.add_argument("message", type=str, help="The commit message")
    args = parser.parse_args()
    
    git_commit(args.directory, args.message)
