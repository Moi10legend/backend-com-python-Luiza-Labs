#1) Use o gerenciamento de contexto (context manager) com a declaração with. Isso permite que os arquivos sejam
#fechados corretamente mesmo em caso de exceções

from pathlib import Path

ROOT_PATH = Path(__file__).parent

# with open(ROOT_PATH / "manipulando arquivos.txt", "r") as arquivo:
#     print(arquivo.read())

#2) Verifique se o arquivo foi aberto com sucesso

# try:
#     with open(ROOT_PATH / "manipulando arquivos.txt", "r") as arquivo:
#         print(arquivo.read())
# except IOError as exc:
#     print("Não foi possível abrir o arquivo")
#     print(exc)

#3) Use a codificação correta
with open(ROOT_PATH / "manipulando arquivos.txt", "r", encoding="UTF-8") as arquivo:
    print(arquivo.read())