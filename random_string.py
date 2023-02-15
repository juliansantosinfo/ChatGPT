import os
import random
import string
import time
import datetime

def random_string(stringLength=600):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))

def main():
    dir_path = "D:\\Documents\\Python\ChatGPT\\files\\"
    filename = datetime.datetime.now().isoformat().replace(":","").replace("-","").replace(".","")
    filename = os.path.join(dir_path, f"minha_lista_{filename}.txt")
    with open(filename, "w") as f:
        f.write(random_string())
    os.system(f'cd {dir_path}')
    os.system(f'git add .')
    os.system(f'git -C {dir_path} commit -am "Atualizado"')
    os.system(f'git push origin master')

if __name__ == "__main__":
    main()
