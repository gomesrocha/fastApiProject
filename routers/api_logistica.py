from fastapi import APIRouter
from domain.AnalisarFormaDeTransforte import analisar_clima_para_entrega
from schema.apiOut import ApiOut
from dotenv import load_dotenv
from functools import lru_cache
from schema.settings import Settings

load_dotenv()


router = APIRouter()

@router.get("/entrega/{cep}")
async  def forma_de_entrega(cep: str):

    return analisar_clima_para_entrega(cep)