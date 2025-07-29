# # from fastapi import APIRouter, Depends, HTTPException, status
# # from sqlalchemy.orm import Session
# # from app.db.session import get_db
# # from app.schemas.user import UserCreate
# # from app.models import User
# # from app.utils import hashing

# # router = APIRouter(prefix="/register", tags=["Auth"])

# # @router.post("/")
# # def register(user: UserCreate, db: Session = Depends(get_db)):
# #     existing_user = db.query(models.User).filter(models.User.email == user.email).first()
# #     if existing_user:
# #         raise HTTPException(status_code=400, detail="Email already registered")
    
# #     new_user = User.User(
# #         username=user.username,
# #         email=user.email,
# #         password_hash=hashing.hash_password(user.password)
# #     )
# #     db.add(new_user)
# #     db.commit()
# #     db.refresh(new_user)
# #     return {"msg": "User created successfully", "user_id": new_user.id}


# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from app.db.session import get_db
# from app.schemas.user import UserCreate, UserOut
# from app.models.user import User
# from app.utils.hashing import hash_password

# router = APIRouter(prefix="/auth", tags=["Auth"])

# @router.post("/register", response_model=UserOut)
# def register(user: UserCreate, db: Session = Depends(get_db)):
#     existing_user = db.query(User).filter(User.email == user.email).first()
#     if existing_user:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
#     new_user = User(
#         username=user.username,
#         email=user.email,
#         password_hash=hash_password(user.password)
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
