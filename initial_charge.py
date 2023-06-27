import asyncio
import logging

import requests
from requests import RequestException, Timeout, TooManyRedirects

from config import configs
from log import logger, configure_loggng
from service.message_service import send_message_to_queue

configure_loggng()

logging.getLogger(__name__)


def get_brands() -> None:
    try:
        response = requests.get(configs.API_URL).json()
        for brand in response:
            asyncio.run(send_message_to_queue(message=brand))
    except (RequestException, Timeout, TooManyRedirects, ConnectionError) as e:
        logger.exception("An exception occurred during the request:", e)
        return

    return response


logger.info("[Carga Inicial-] Starting data load")
get_brands()
logger.info("[Carga Inicial-] charge completed")

