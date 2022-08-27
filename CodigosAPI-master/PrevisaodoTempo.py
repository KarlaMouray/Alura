#Aqui importamos as bibliotecas que vamos usar
import requests,json

#Um pequeno cabeçalho decorado para agradar aos olhos de quem vê.
print('-=' *15)
print('-= PREVISÃO DO TEMPO =-')
print('-=' *15)

#Configurando a chave API.
chaveapi = "INSIRA_AQUI_A_CHAVE" #Chave cadastrada no site openweathermap.org

#Perguntamos qual a cidade que desejamos saber como está o tempo?
cidade = input('Para qual cidade você deseja consultar o tempo neste momento? ')

#Fazemos na linha abaixo a coleta das informações da API via JSON.
res = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}'.format(cidade,chaveapi))
resposta = res.json()

#Aqui fatiamos as listas e dicionários para pegar as informações bem como transformamos Kelvin em Celsius.
clima = resposta['weather']
temperatura = resposta['main']
sensacao = resposta['main']
tkelvin = temperatura['temp']
tcelsius = float(tkelvin - 273.15)
skelvin = temperatura['feels_like']
scelsius = float(skelvin - 273.15)

#E aqui começamos a dar as respostas, com certa decoração, de como está o tempo na cidade digitada.
print('-=' *15)
print('A cidade de {} neste momento está {}'.format(cidade,clima[0]['main']))
print('O céu está {}'.format(clima[0]['description']))
print('A temperatura é de {}º Celsius e a sensação térmica {}º Celsius'.format(round(tcelsius,1),(round(scelsius,1))))
print('A pressão atmosférica é de {}'.format(temperatura['pressure']))
print('A umidade relativa do ar é de {}%'.format(temperatura['humidity']))