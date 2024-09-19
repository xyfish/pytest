from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user import UserCreate

# 創建新用戶
def create_user(db: Session, user: UserCreate):
    hashed_password = user.password + "notreallyhashed"  # 假設這裡處理密碼哈希
    db_user = UserModel(name=user.name, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 根據ID獲取用戶
def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()

# 根據Email獲取用戶
def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

# 獲取所有用戶
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()

# 刪除用戶
def delete_user(db: Session, user_id: int):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    db.delete(user)
    db.commit()
    return user

# 更新用戶
def update_user(db: Session, user_id: int, name: str):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    user.name = name
    db.commit()
    db.refresh(user)
    return user
