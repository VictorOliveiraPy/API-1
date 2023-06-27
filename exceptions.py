from fastapi import HTTPException


class VehicleNotFoundException(HTTPException):
    def __init__(self, codigo_marca: int):
        detail = f"Vehicle with code {codigo_marca} not found"
        super().__init__(status_code=404, detail=detail)
