from genericpath import exists
from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

app = FastAPI()

inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The Id of the Item youd like to view",gt=0, lt=10)):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(*, name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data" : "Not Found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists."}
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item ID does not exist"}
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    inventory[item_id].update(item)
    return inventory[item_id]


@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The id of the item to delete", gt=0)):
    if item_id not in inventory:
        return {"Error": "ID does not exisit"}

    del inventory[item_id]
    return {"Succes": "Item deleted"}


