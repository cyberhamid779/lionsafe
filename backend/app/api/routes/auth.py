from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.services.auth import authenticate_admin, create_access_token, hash_password
from app.services.database import get_db
from app.models.organization import Organization
from app.models.user import User

router = APIRouter()


class RegisterRequest(BaseModel):
    company_name: str
    email: EmailStr
    password: str


@router.post("/register", status_code=201)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Bu email artıq qeydiyyatdadır")

    domain = data.email.split("@")[1]
    existing_org = db.query(Organization).filter(Organization.domain == domain).first()
    if existing_org:
        raise HTTPException(status_code=400, detail="Bu domain artıq qeydiyyatdadır")

    org = Organization(name=data.company_name, domain=domain)
    db.add(org)
    try:
        db.flush()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Bu domain artıq qeydiyyatdadır")

    admin = User(
        org_id=org.id,
        email=data.email,
        name=data.company_name,
        is_admin=True,
        hashed_password=hash_password(data.password),
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)

    token = create_access_token({"sub": str(admin.id), "org": org.id})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_admin(db, form.username, form.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Yanlış email və ya şifrə")
    token = create_access_token({"sub": str(user.id), "org": user.org_id})
    return {"access_token": token, "token_type": "bearer"}
