from pydantic import BaseModel, ConfigDict

class PaymentCreate(BaseModel):
    """Request schema khi tạo payment"""
    amount: float
    team_id: int
    payer_id: int
    description: str


class PaymentResponse(PaymentCreate):
    """Response schema trả về sau khi payment được xử lý"""
    id: int
    status: str

    # Pydantic v2: bật "from_attributes" để có thể đọc từ ORM objects
    model_config = ConfigDict(from_attributes=True)