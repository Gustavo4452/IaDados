import requests

cep = input("digite seu cep: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url)
respostas = dados.json()

print(f"você mora na rua {respostas["logradouro"]}. No bairro {respostas["bairro"]}. Na cidade de {respostas["localidade"]}")
      











