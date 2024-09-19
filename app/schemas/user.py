from pydantic import BaseModel, EmailStr

# 用於創建新用戶時的數據驗證
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

# 用於回應中返回用戶數據
class User(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
