from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api_logger")

app = FastAPI()

# In-memory storage (acts like a mock database)
database = {}

# Pydantic model for the item
class Item(BaseModel):
    id: int
    name: str
    value: int

# CREATE
@app.post("/items/")
def create_item(item: Item):
    if item.id in database:
        raise HTTPException(status_code=400, detail="Item already exists")
    database[item.id] = item
    logger.info(f"Item created: {item}")
    return {"message": "Item created", "item": item}

# READ with multiple query parameters
@app.get("/add/")
def add_values(a: int, b: int, c: int = 0):
    result = a + b + c
    logger.info(f"GET params: a={a}, b={b}, c={c} | sum={result}")
    return {"sum": result}

# READ single item
@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = database.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    logger.info(f"Item retrieved: {item}")
    return item

# UPDATE
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in database:
        raise HTTPException(status_code=404, detail="Item not found")
    database[item_id] = item
    logger.info(f"Item updated: {item}")
    return {"message": "Item updated", "item": item}

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in database:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = database.pop(item_id)
    logger.info(f"Item deleted: {deleted_item}")
    return {"message": "Item deleted"}
