from typing import Annotated
from pydantic import  Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta',example="Joao", max_lenght=50)]
    cpf:  Annotated[str, Field(description='Cpf  do Atleta',example="11111111111", max_lenght=11)]
    idade:  Annotated[int, Field(description='Idade do Atleta',example=22)]
    peso:  Annotated[ PositiveFloat, Field(description='Peso do Atleta',example=80.5)]
    altura:  Annotated[ PositiveFloat, Field(description='Altura do Atleta',example=170.6)]
    sexo:  Annotated[str, Field(description='Sexo  do Atleta', example='M', max_lenght=1)]