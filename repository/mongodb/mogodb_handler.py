import logging

from pymongo import MongoClient

from config import configs
from exceptions import VehicleNotFoundException
from log import logger, configure_loggng

configure_loggng()

logging.getLogger(__name__)

client = MongoClient(configs.HOST_DB)
db = client["test"]
collection = db["marcas"]


def get_brands_db():
    try:
        brand_data = list(collection.find({}, {'_id': 0}))
        return brand_data
    except Exception as e:
        logger.exception(f"Error occurred while fetching brands from the database: {str(e)}")
        return None
    finally:
        client.close()


def get_vehicles(cod):
    try:
        filter_cod = {'modelos.codigo': cod}
        vehicle = collection.find_one(filter_cod, {'_id': 0, 'modelos.$': 1, 'anos': 1})
        client.close()
        if not vehicle:
            raise VehicleNotFoundException(cod)
        return vehicle
    except VehicleNotFoundException as e:
        logger.exception(f"Error occurred while fetching the vehicle with code {cod}: {str(e)}")
        return None
    except Exception as e:
        logger.exception(f"Error occurred while fetching vehicle with code {cod}: {str(e)}")
        return None
    finally:
        client.close()
