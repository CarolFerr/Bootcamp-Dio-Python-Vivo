# fazer validações
# Quando se utiliza o pydantic é necessário importar a classe BaseModel, essa será herdada posteriormente
from typing import Annotated

from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema


class Atleta(BaseSchema):
    # Field ajuda a detalhar o campo
    nome: Annotated[str, Field(description='Nome do Atleta', example='Ana', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', example=46)]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', example=65.8)]
    altura: Annotated[PositiveFloat, Field(description='Altura do Atleta', example=1.65)]
    sexo: Annotated[str, Field(description='Sexo do Atleta', example='F', max_length=1)]
    