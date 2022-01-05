from datetime import date
from typing import List

from pydantic import BaseModel


class XYDataModel(BaseModel):
    date: date
    value: float


class DataModel(BaseModel):
    x_data_type: str
    y_data_type: str
    x: List[XYDataModel]
    y: List[XYDataModel]


class DataInModel(BaseModel):
    user_id: int
    data: DataModel
