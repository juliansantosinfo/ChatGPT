import os
import random
import string
import time
import datetime

dir_path = "D:\\Documents\\Python\ChatGPT\\"
filename = datetime.datetime.now().isoformat().replace(":","").replace("-","").replace(".","")
filename = os.path.join(dir_path, f"minha_lista_{filename}.txt")

def random_string(stringLength=600):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))

def main():
    with open(filename, "w") as f:
        f.write(random_string())
    os.system(f'git -C {dir_path} commit -am "Atualizado"')

if __name__ == "__main__":
    while True:
        main()
        time.sleep(60 * 20)
