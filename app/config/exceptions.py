from fastapi import status
from fastapi.exceptions import HTTPException

shipped_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Order is shipped",
)

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid username or password",
    headers={"WWW-Authenticate": "Bearer"},
)

token_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid or expired token",
    headers={"WWW-Authenticate": "Bearer"},
)

permission_exception = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="Permission denied",
)

not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Not Found",
)

exists_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Already exists",
)

stock_exception = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Out of stock",
)

server_exception = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Internal server error",
)
