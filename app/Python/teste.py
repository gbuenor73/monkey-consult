import pyodide_http
import requests

pyodide_http.patch_all()

url = 'http://localhost:5000/clientes?id=1'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Falha na requisição:', response.status_code)
