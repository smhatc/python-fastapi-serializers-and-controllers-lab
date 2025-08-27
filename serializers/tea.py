from pydantic import BaseModel, Field
from typing import Optional, List
from .comment import CommentSchema
from .user import UserResponseSchema

class TeaSchema(BaseModel):
  id: Optional[int] = Field(default=None) # This makes sure you don't have to explicitly add an id when sending json data
  name: str
  in_stock: bool
  rating: int
  comments: List[CommentSchema] = []

  # Relationships
  comments: List[CommentSchema] = []
  user: UserResponseSchema

  class Config:
    orm_mode = True

class TeaCreateSchema(BaseModel):
  name: str
  in_stock: bool
  rating: int