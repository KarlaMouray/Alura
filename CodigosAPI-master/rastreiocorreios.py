#RASTREIO Correios 1.1

#importa as bibliotecas
import requests

#cabeçalho decorado
print('###'*25)
print('  RASTREIO DE ENCOMENDAS 1.1')
print('###'*25)

#Pega com o usuário o código da encomenda
codigo_rastreio = input('Digite o código de rastreio para a consulta: ')

#faz a conexão com a API da ViaCep
request = requests.get('https://proxyapp.correios.com.br/v1/sro-rastro/{}'.format(codigo_rastreio))
resp_consulta = (request.json())
print(resp_consulta['objetos'][0]['eventos'][1])
#print(resp_consulta)
listaeventos = []
listaeventos2 = []
i = 0
#Se o código de rastreio for válido, vai fazer as devidas extrações com o JSON retornado dos Correios
#e vai retornar a resposta.
#try:
while i < len(resp_consulta['objetos'][0]['eventos']):
    listaeventos.append(resp_consulta['objetos'][0]['eventos'][i])
    i += 1

controle = 0
for c in listaeventos:
    listaeventos2.append(listaeventos[controle])
    controle += 1

print('=-='*25)
print('=== PESQUISANDO ENCOMENDA NÚMERO {} ==='.format(codigo_rastreio))
for x in range(len(listaeventos2)):
    print('|| Data: {}'.format(listaeventos2[x]['dtHrCriado']))
    print('|| Situação: [{}] - {}'.format(listaeventos2[x]['codigo'],listaeventos2[x]['descricao']))
    print('=-=' * 25)
    x += 1

#Se der erro e o código não estiver obsoleto, vai informar que o código ainda não foi postado ou é inválido.
#except:
print(listaeventos2)
print('Objeto não localizado ou código inválido. Verifique o código e se ele foi postado e tente novamente!')

