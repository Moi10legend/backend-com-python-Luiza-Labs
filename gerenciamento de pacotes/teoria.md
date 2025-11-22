# O PIP 
é gerenciador de pacotes do Python, nos permitindo instalar, atualizar e remover pacotes.
Ele se comunica com o PyPI (Python Package Index), que é onde a maioria dos pacotes são armazenados,
também podemos entrar no site do PyPI para ver os pacotes disponíveis.

Comando para instalar pacotes:
pip install [nome do pacote] 

Comando para desinstalar pacotes:
pip uninstall [nome do pacote]

Comando para listar todas as bibliotecas instaladas no seu interpretador:
pip list

Comando para atualizar o pacote:
pip install --upgrade [nome do pacote]

Comando para procurar por pacotes:
pip search [termo de busca]

OBS: O pip não consegue desinstalar os pacotes e suas depêndencias de uma só vez.

Ambientes virtuais
Como os criados por venvs, nos permitem manter as dependências de diferentes projetos. Isso é importante
para evitar conflitos entre versões de pacotes.

Para criar um ambiente virtual utiliza-se o seguinte comando:
python3 -m venv [nome do ambiente]
source myenv/bin/activate

Comando para desativar o ambiente virtual:
deactivate

# Pipenv
É uma ferramenta de gerenciamento de pacotes que combina a gestão de dependências com a criação de um
ambiente virtual para seus projetos e adiciona/remove pacotes automaticamente do arquivo Pipfile conforme
você instala ou desinstala pacotes.

Comando para instalar o Pipenv:
pip install pipenv

comando para instalar pacotes com pipenv:
pipenv install [nome do pacote]

comando para desinstalar pacotes com pipenv:
pipenv uninstall [nome do pacote]

comando para criar o arquivo de lock:
pipenv lock

comando para listar todas as dependências:
pipenv graph

comando para remover as dependências:
pipenv clean


# Poetry

Outra ferramenta de gestão de dependências para Python. Também suporta o empacotamento e publicação de projetos no PyPI.

Para instalar o poetry:
pip install poetry

Para criar um projeto do zero:
poetry new [nome do projeto]

Para adicionar uma dependência:
poetry add [dependência]

Para remover uma dependência:
poetry remove [dependência]

Para iniciar o poetry em um projeto já existente:
poetry init

OBS: O poetry remove de forma automática um pacote e suas dependências.