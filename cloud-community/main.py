from fastapi import FastAPI
from schemas.user import UserCreate, UserResponse

app = FastAPI()

# 서버 실행 test endpoint
@app.get("/")
def root():
    return {"Test"}


# Pydantic Schemas를 request body
@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    
    # 실제 DB 대신 임시 데이터 반환
    return UserResponse(
        id=1,
        username=user.username,
        email=user.email
    )