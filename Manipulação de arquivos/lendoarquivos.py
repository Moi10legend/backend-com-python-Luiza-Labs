#Para abrir um arquivo, utiliza-se a função open()
#e para fechar é a função close()

arquivo = open("manipulando arquivos.txt", "r")

#O 'r' é o modo de abertura do arquivo, significa leitura.
#Existem outros modos de abertura como 'w' que é gravação e 'a' que é anexar

print(arquivo.read())

while len(linha := arquivo.readline()):
    print(linha)

arquivo_lista = arquivo.readlines()

#Para e leitura de um arquivo existe o read() que lê todo o conteúdo do arquivo de uma vez
#readline() que lê uma linha por vez e o readlines() que retorna uma lista onde cada elemento
#é uma linha do arquivo

arquivo.close()