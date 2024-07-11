from 

from workout_api.contrib.schemas import BaseSchema


class categoria(BaseSchema):
    nome: Annotated(str, Field(description='Nome da categoria', example='Scale', max_lenght=10))