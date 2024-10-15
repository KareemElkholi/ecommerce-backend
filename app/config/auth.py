from datetime import datetime, timedelta, timezone
from os import getenv

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import decode, encode
from jwt.exceptions import InvalidTokenError

from app.config.exceptions import permission_exception, token_exception

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_token(data: dict):
    exp = datetime.now(timezone.utc) + timedelta(minutes=int(getenv("EXPIRE")))
    data.update({"exp": exp})
    return encode(data, getenv("SECRET_KEY"), algorithm=getenv("ALGORITHM"))


def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        return decode(token, getenv("SECRET_KEY"), algorithms=[getenv("ALGORITHM")])
    except InvalidTokenError:
        raise token_exception


def verify_permission(payload: dict = Depends(verify_token)):
    if payload.get("role") != "admin":
        raise permission_exception
    return payload
