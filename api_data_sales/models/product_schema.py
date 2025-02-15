from typing import List

from pydantic import BaseModel


class Product(BaseModel):
    id: str
    nome_produto: str
    categoria: str
    total_vendido: int
    total_receita: float
    estoque_atual: int


class CategoryList(BaseModel):
    categories: List[str]


class QuantityResponse(BaseModel):
    quantity: int


class TotalQuantityCategory(BaseModel):
    category: str
    quantity: int


class TotalQuantityByCategory(BaseModel):
    data: List[TotalQuantityCategory]
