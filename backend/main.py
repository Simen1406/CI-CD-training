from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

from db.db_helpers import retrieve_db_items

app = FastAPI(title="CI/CD Demo API")

# In-memory "database"
items_db: dict[int, dict] = {}
next_id: int = 1


class ItemCreate(BaseModel):
    name: str
    description: str = ""
    price: float = Field(gt=0)


class ItemOut(ItemCreate):
    id: int


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items", response_model=list[ItemOut])
def list_items():
    food_items = retrieve_db_items()
    print("Food items from DB:", food_items)

    return food_items


@app.post("/items", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate):
    global next_id
    new_item = {"id": next_id, **item.model_dump()}
    items_db[next_id] = new_item
    next_id += 1
    return new_item


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
