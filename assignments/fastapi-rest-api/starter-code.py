from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float

items: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment!"}

@app.get("/items")
def list_items():
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    # TODO: Return the item with this ID or raise HTTPException(status_code=404)
    pass

@app.post("/items")
def create_item(item: Item):
    # TODO: Add the new item to the items list and return it
    pass

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    # TODO: Update the item with the given ID or raise HTTPException(status_code=404)
    pass

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # TODO: Remove the item with the given ID or raise HTTPException(status_code=404)
    pass

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
