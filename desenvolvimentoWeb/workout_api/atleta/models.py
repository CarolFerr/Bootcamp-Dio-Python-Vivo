from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from workout_api.categorias.models import CategoriaModel
from workout_api.centro_de_treinamento.models import CentroTreinamentoModel
from workout_api.contrib.models import BaseModel


class AtletaModel(BaseModel):
    __table__ = 'atletas'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    # Relacionamento de Atleta com categoria
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atleta')
    #   Para poder acessar no bando de dados
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
    centro_de_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atleta')
    centro_de_treinamento_id: Mapped[int] = mapped_column(ForeignKey('centro_de_treinamento.pk_id'))
