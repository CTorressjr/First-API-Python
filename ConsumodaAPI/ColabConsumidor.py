!pip install requests

import requests

link = 'https://MinhaAPI.carlostorres44.repl.co/endpoint2'

req = requests.get(link)

print(req)
print(req.json())

dicionario = req.json()

print(dicionario['total_vendas'])
