from typing import List

from pydantic import BaseModel


class QuantityFloatResponse(BaseModel):
    quantity: float

    