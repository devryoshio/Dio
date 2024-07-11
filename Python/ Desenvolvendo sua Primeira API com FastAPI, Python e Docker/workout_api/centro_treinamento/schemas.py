from typing import Annotated
from workout_api.contrib.schemas import BaseSchema
from pydantic import Field


class CentroTreinamento(BaseSchema):
    nome: Annotated(str, Field(description='Nome do Centro de Treinamento', example='Max treinamento', max_lenght=20))
    endereco: Annotated(str, Field(description='Endereço do Centro de Treinamento', example='Avenida Brasil, 101, Bairro Limoeiro, Cidade de Deus-RJ', max_lenght=60))
    proprietario: Annotated(str, Field(description='Nome do proprietario do Centro de Treinamento', example='Julius Batista', max_lenght=30))