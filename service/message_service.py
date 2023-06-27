import json

import aio_pika

from config import configs


async def send_message_to_queue(message) -> None:
    connection = await aio_pika.connect_robust(
        configs.BROKER_URL
    )

    async with connection:
        routing_key = configs.QUEUE_NAME

        channel = await connection.channel()

        await channel.default_exchange.publish(
            aio_pika.Message(body=json.dumps(message).encode()),
            routing_key=routing_key,
        )