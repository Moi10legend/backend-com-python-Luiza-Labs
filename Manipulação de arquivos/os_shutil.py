import os
import shutil
from pathlib import Path

#ROOT_PATH = Path(__file__)  #Irá retornar o caminho até o arquivo atual que está sendo manipulado
#print(ROOT_PATH)

ROOT_PATH = Path(__file__).parent  #Retorna o diretório em que está o arquivo atual que está sendo manipulado
#print(ROOT_PATH.parent)

#vai criar um novo diretório
#os.mkdir(ROOT_PATH / "Novo-diretório")

#arquivo = open(ROOT_PATH / "Novo arquivo.txt", "w")

#arquivo.close()

#Renomeia o nome do arquivo
#os.rename(ROOT_PATH / "Novo-diretório" / "Novo arquivo.txt", ROOT_PATH / "Novo-diretório" / "Alterado.txt")

#Remove um arquivo
#os.remove(ROOT_PATH / "Novo-diretório" / "Novo arquivo.txt")

#Move um arquivo de local
#shutil.move(ROOT_PATH / "Novo arquivo.txt", ROOT_PATH / "Novo-diretório" / "Novo arquivo.txt")

