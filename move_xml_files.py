import os
import shutil
import sys

def move_xml_files(src_dir, dst_dir, search_string = None):
    # Verifica se o diretório de origem existe
    if not os.path.isdir(src_dir):
        print(f"O diretório de origem {src_dir} não existe")
        return

    # Verifica se o diretório de destino existe
    if not os.path.isdir(dst_dir):
        print(f"O diretório de destino {dst_dir} não existe")
        return

    # Percorre todos os arquivos e subdiretórios no diretório de origem
    for dirpath, dirnames, filenames in os.walk(src_dir):
        for filename in filenames:
            # Verifica se o arquivo tem a extensão .xml
            if filename.endswith(".xml"):
                # Verifica se a string de busca foi informada e se o nome do arquivo contém a string
                if search_string and search_string not in filename:
                    continue
                src_path = os.path.join(dirpath, filename)
                dst_path = os.path.join(dst_dir, os.path.relpath(src_path, src_dir))
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                shutil.move(src_path, dst_path)
                print(f"Arquivo {filename} movido com sucesso.")

# Valida se os parâmetros de diretório foram passados na linha de comando
if len(sys.argv) < 3:
    print("Uso: python script.py <diretorio_origem> <diretorio_destino> [string_de_busca]")
    sys.exit(1)

src_dir = sys.argv[1]
dst_dir = sys.argv[2]
search_string = None if len(sys.argv) == 2 else sys.argv[3]

move_xml_files(src_dir, dst_dir, search_string)
