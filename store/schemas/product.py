from decimal import Decimal
from typing import Annotated, Optional
from bson import Decimal128
from pydantic import AfterValidator, Field
from store.schemas.base import BaseSchemaMixin, OutSchema


class ProductBase(BaseSchemaMixin):
    name: str = Field(..., description="Nome do produto")
    quantity: int = Field(..., description="Quantidade do produto")
    price: Decimal = Field(..., description="Preço do produto")
    status: bool = Field(..., description="Status do produto")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn, OutSchema):
    ...


def convert_decimal_128(v):
    return Decimal128(str(v))


Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class ProductUpdate(BaseSchemaMixin):
    quantity: Optional[int] = Field(None, description="Quantidade do produto")
    price: Optional[Decimal_] = Field(None, description="Preço do produto")
    status: Optional[bool] = Field(None, description="Status do produto")


class ProductUpdateOut(ProductOut):
    ...
