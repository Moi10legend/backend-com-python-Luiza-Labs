#Exceções mais comuns:
#FileNotFoundError: Quando o arquivo que está sendo aberto não é encontrado no caminho especificado
#PermissionError: Quando a tentativa de abrir o arquivo falha por não ter as permissões necessárias para leitura ou gravação
#IOError: Quando ocorre um erro geral de E/S ao trabalhar com o arquivo.
#UnicodeDecodeError: Quando ocorre um erro ao decodificar os dados de um arquivo de texto usando uma codificação inadequada.
#UnicodeEncodeError: Quando ocorre um erro ao tentar codificar dados em uma determinada codificação ao gravar em um arquivo de texto.
#IsADirectoryError: Quando é feita uma tentativa de abrir um diretório em ves de um arquivo de texto

try:
    arquivo = open("Meu arquivo.py")

except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc) #Dá os detalhes da exceção
except IsADirectoryError as exc:
    print("O caminho é um diretório")
    print(exc)