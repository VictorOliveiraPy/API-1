from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    BROKER_URL: str = "amqp://admin:pass@127.0.0.1/"
    API_URL: str = "https://parallelum.com.br/fipe/api/v1/carros/marcas"
    HOST_DB: str = "mongodb://root:password@127.0.0.1"
    QUEUE_NAME: str = "test_queue"


configs = Config()
