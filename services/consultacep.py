import httpx

url = 'https://viacep.com.br/ws/{}/json/'

def cidade_por_cep(cep):
    resposta = httpx.get(url.format(cep))
    if resposta.status_code == 200:
        cidade = resposta.json()['localidade']
    return cidade

