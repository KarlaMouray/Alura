#ConsultaCEP

#importa as bibliotecas
import requests

# cabeçalho decorado
print('########################')
print(' CONSULTA CEP 1.1')
print('########################')

#pega o cep
cep = input('Digite o CEP para a consulta: ')

#verifica o cep válido
if len(cep) != 8:
    print('CEP inválido. Tente novamente!')
    exit()

#faz a conexão com a API da ViaCep
request = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))
dadosendereco = (request.json())

#Verifica se o CEP existe e retorna seus dados.
if 'erro' not in dadosendereco:
    #print(dadosendereco)
    print('#########################')
    print('# Resultado da consulta #')
    print('CEP: {}'.format(dadosendereco['cep']))
    print('Logradouro: {}'.format(dadosendereco['logradouro']))
    print('Complemento: {}'.format(dadosendereco['complemento']))
    print('Bairro: {}'.format(dadosendereco['bairro']))
    print('Município: {}'.format(dadosendereco['localidade']))
    print('UF : {}'.format(dadosendereco['uf']))
    print('#########################')

else:
    print('CEP inválido!')