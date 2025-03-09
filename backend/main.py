""""Backend Main block"""
import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from helpers.constants import SECRET_LIST
from helpers.config_loader import load_secrets

# Init 
app = FastAPI(title="CA-Backend")

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.on_event("startup")
async def startup_event():
    load_secrets(SECRET_LIST)
    #Get storage data as a cache

@app.get("/")
def read_root():
    #load_secrets(SECRET_LIST)
    return {"Hello": os.environ.get("STORAGE-ACCOUNT-NAME")}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

