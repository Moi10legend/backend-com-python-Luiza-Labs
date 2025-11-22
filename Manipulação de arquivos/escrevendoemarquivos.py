arquivo = open("manipulando arquivos.txt", "w")

arquivo.write("Hoje é sábado")
arquivo.writelines(["Amanhã", "é", "Domingo"])

arquivo.close()