from pydantic import BaseModel

# 회원 생성을 위한 Pydantic schemas
class UserCreate(BaseModel):
    username: str
    email: str


# 회원 응답용 schemas
class UserResponse(BaseModel):
    id: int
    username: str
    email: str