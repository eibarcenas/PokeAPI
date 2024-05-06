from fastapi import HTTPException


class BerriesNamesNotFound(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(
            status_code=status_code,
            detail=detail,
        )


class BerryNotFound(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(
            status_code=status_code,
            detail=detail,
        )
