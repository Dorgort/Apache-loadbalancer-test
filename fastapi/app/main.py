from fastapi import FastAPI
import asyncio
from time import sleep
app = FastAPI()


@app.get("/")
async def hello_world():
    await asyncio.sleep(5)
    sleep(5)
    return {"message": "Number1"}
