from typing import Optional

from pydantic import BaseModel


class Product_Wildberies(BaseModel):
    name: Optional[str]
    brand: Optional[str]
    brand_id: Optional[int]
    site_brand_id: Optional[int]
    supplier_id: Optional[int]
    sale: Optional[int]
    price: Optional[int]
    sale_price: Optional[int]
    rating: Optional[int]
    feedbacks: Optional[int]
    colors: Optional[str]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True