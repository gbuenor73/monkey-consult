import requests

# URL de exemplo
url = 'localhost:5000/clientes?id=1'

# Fazendo a requisição GET
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida (código 200)
if response.status_code == 200:
    # Extraindo os dados da resposta (JSON no caso)
    data = response.json()
    print(data)
else:
    print('Falha na requisição:', response.status_code)
