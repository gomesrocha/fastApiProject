from pydantic import BaseSettings

'''ApiOut é o Schema de dados para a resposta a solicitação do usuário'''
class ApiOut(BaseSettings):
    '''Temperatura'''
    temp: float
    '''Clima na região'''
    weather: str
    '''Cidade da entrega'''
    city: str
    '''Indicação de tipo de transporte'''
    type_of_transport: str