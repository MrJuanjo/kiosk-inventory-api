from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    category: str | None = Field(default=None, max_length=100)
    stock_quantity: int = Field(default=0, ge=0)
    has_discount: bool | None = Field(default=False)


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int

    model_config = {"from_attributes": True}
