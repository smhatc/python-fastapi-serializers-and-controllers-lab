from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str  # User's unique name
    email: str  # User's email address
    password: str  # Plain text password for user registration (will be hashed before saving)

    class Config:
        orm_mode = True  # Enables compatibility with ORM models

# Schema for returning user data (without exposing the password)
class UserResponseSchema(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True
