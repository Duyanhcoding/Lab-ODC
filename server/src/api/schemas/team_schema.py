from pydantic import BaseModel
from typing import List, Optional

class TeamMemberCreate(BaseModel):
    user_id: int
    role: str = "MEMBER"

class TeamCreate(BaseModel):
    name: str
    project_id: Optional[int] = None

class TeamResponse(TeamCreate):
    id: int
    wallet_balance: float
    class Config:
        from_attributes = True