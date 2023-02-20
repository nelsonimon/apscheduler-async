from time import sleep
from typing import Union
from fastapi import FastAPI

app = FastAPI(title="FastAPI and Async APScheduler",docs_url="/")


@app.get("/hello_world")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    print('app items - beggin')
    sleep(10)
    return {"item_id": item_id, "q": q}