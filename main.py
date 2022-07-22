from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
    }
}

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The Id of the Item youd like to view",gt=0, lt=2)):
    return inventory[item_id]

@app.get("/get-by-name/")
def get_item(*, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data" : "Not Found"}

@app.get("/create-item")
def create_item(item: Item):
    return {"Data": "data"}


@app.get("/")
def home():
    return {"Message" : "Welcome to our page"}



@app.get("/about")
def about():
    return {"Data" : "About"}



