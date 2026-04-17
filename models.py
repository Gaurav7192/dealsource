from pydantic import BaseModel, ConfigDict
from datetime import date, datetime
from typing import Optional


class SaleBase(BaseModel):# this is a model or schema for i phone sale
    customer_name: str
    phone_model: str
    color: str
    storage_gb: int
    price: float
    sale_date: date
    store_location: str


class SaleCreate(SaleBase):
    pass


class Sale(SaleBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True) # this is used to create data creating time and it is automatic fatch current time