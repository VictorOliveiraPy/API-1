from fastapi import APIRouter

from exceptions import VehicleNotFoundException
from repository.mongodb.mogodb_handler import get_brands_db, get_vehicles

brand_router = APIRouter()


@brand_router.get("", status_code=200)
def get_brands():
    return get_brands_db()


@brand_router.get('/vehicles')
def vehicle_brand(codigo_marca: int):
    vehicle = get_vehicles(codigo_marca)
    if not vehicle:
        raise VehicleNotFoundException(codigo_marca)

    return {'vehicles': vehicle}
