from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ItemRequest(BaseModel):
    name: str
    quantity: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}", "available": True}

@app.post("/items")
def create_item(item: ItemRequest):
    return {"message": "Item received", "item": item}

# To run this app locally, use:
# uvicorn --app-dir assignments/fastapi-rest-api starter-code:app --reload
