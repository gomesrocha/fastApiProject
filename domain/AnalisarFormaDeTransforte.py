from schema.apiOut import ApiOut

from services import consultatempo, consultacep

def analisar_clima_para_entrega(cep):
    if len(cep) == 8:
        local = consultacep.cidade_por_cep(cep)
    if len(local) > 0:
        (temperatura, clima) = consultatempo.temperatura_por_localidade(local)
    if clima == "Rain":
        transporte="carro"
    else:
        transporte="moto"
    mensagem = f"O transporte preferivel neste tempo será: {transporte}"
    return ApiOut(temp=temperatura, weather=clima, city=local, type_of_transport=mensagem)