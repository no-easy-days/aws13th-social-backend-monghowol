from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"FastAPI 프로젝트 생성 및 실행 확인"}