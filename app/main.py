from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from app.api.v1.endpoints import users

from app.db.session import Base, engine

# 創建所有表
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# 包含用戶的路由
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI User API"}
