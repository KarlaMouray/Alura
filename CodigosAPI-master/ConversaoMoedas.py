#Importa as bibliotecas
import requests, json

#Cabeçalho decorado
print('-='*15)
print('-= COTAÇÃO DE MOEDAS =-')
print('-='*15)

#entra com a opção de moeda
escolha = input('Qual moeda você deseja saber a sua cotação? [1] Dólar, [2] Euro ou [3] Bitcoin: ')

#Condiciona as escolhas e faz as consultas na API do AwesomeAPI
if escolha == "1":
    res = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    resposta = res.json()
    chave = resposta['USDBRL']
    moeda = "Dólar"
elif escolha == "2":
    res = requests.get('https://economia.awesomeapi.com.br/last/EUR-BRL')
    resposta = res.json()
    chave = resposta['EURBRL']
    moeda = "Euro"
elif escolha == "3":
    res = requests.get('https://economia.awesomeapi.com.br/last/BTC-BRL')
    resposta = res.json()
    chave = resposta['BTCBRL']
    moeda = "Bitcoin"
else:
    print('Opção inválida, programa finalizado. Tente novamente!')

#Exibe a cotação da moeda escolhida contendo a máxima, mínima e variação da cotação diária.
print('Cotação de hoje para {}: \n Máxima: {} \n Mínima {} \n Porcentagem de variação {}'.format(moeda,chave['high'],chave['low'],chave['pctChange']))

#print(res.status_code)
#print(res.headers)
#print(res.text)
#print (resposta)

