#Geradores são tipos especiais de iteradores, não armazenam todos os seus valores na memória.
#São definidos usando funções regulares, mas ao invés de retornarem valores usando o return,
#Utilizam o yield
#Características dos geradores:
#Uma vez que o item gerado é consumido, ele é esquecido e não pode ser acessado novamente
#O estado interno de um gerador é mantido entre chamadas
#A execução de um gerador é pausada na declaração yield e retomada dai na próxima vez que for chamado
import requests

def fetch_products(api_url, max_pages = 100):
    page = 1
    while page <= max_pages:
        response = requests.get(f'{api_url}?page={page}')
        data = response.json()
        for product in data['products']:
            yield product
        if 'next_page' not in data:
            break
        page += 1

#Uso do gerador
for product in fetch_products("http://api.example.com/products"):
    print(product['name'])