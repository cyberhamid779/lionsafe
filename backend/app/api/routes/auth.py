from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.services.auth import authenticate_admin, create_access_token
from app.services.database import get_db

router = APIRouter()


@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_admin(db, form.username, form.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Yanlış email və ya şifrə")
    token = create_access_token({"sub": str(user.id), "org": user.org_id})
    return {"access_token": token, "token_type": "bearer"}
