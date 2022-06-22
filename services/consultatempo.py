import httpx
urltempo = 'http://api.openweathermap.org/data/2.5/weather?q={}&lang=pt_br&appid=b77e07f479efe92156376a8b07640ced'

def temperatura_por_localidade(localidade):
    global clima
    resposta = httpx.get(urltempo.format(localidade))
    if resposta.status_code == 200:
        tempo = resposta.json()
        clima = tempo['weather'][0]['main']
        temperatura = float(tempo['main']['temp'])/10
    return temperatura, clima
