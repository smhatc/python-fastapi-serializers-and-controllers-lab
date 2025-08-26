from pydantic import BaseModel, Field
from typing import Optional

class CommentSchema(BaseModel):
  id: Optional[int] = Field(default=None)
  content: str

  class Config:
    orm_mode = True
