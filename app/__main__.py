from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from uvicorn import run

from app.api import api
from app.config.auth import create_token
from app.config.database import get_db
from app.config.exceptions import credentials_exception
from app.config.hashing import verify_password
from app.models.user import User

app = FastAPI()
app.include_router(api.router)


@app.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise credentials_exception
    access_token = create_token({"sub": user.id, "role": user.role.value})
    return {"access_token": access_token, "token_type": "bearer"}


run(app, host="0.0.0.0")
