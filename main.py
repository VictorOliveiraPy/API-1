from fastapi import FastAPI

from controllers.brand import brand_router

app = FastAPI()


@app.get("/health-check/")
async def pong():
    return {"message": "OK"}


app.include_router(brand_router, prefix="/brands")
