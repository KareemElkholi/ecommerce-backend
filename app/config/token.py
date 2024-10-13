from datetime import datetime, timedelta, timezone
from os import getenv
from typing import Annotated

from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer

from jwt import decode, encode
from jwt.exceptions import InvalidTokenError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_token(data: dict):
    exp = datetime.now(timezone.utc) + timedelta(minutes=int(getenv("EXPIRE")))
    data.update({"exp": exp})
    return encode(data, getenv("SECRET_KEY"), algorithm=getenv("ALGORITHM"))


def read_token(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        return decode(token, getenv("SECRET_KEY"), algorithms=[getenv("ALGORITHM")])
    except InvalidTokenError:
        raise credentials_exception
