# Starter code for FastAPI REST API assignment

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Example data model
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

items: List[Item] = []

# TODO: Implement endpoints for CRUD operations

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI REST API!"}

# Add more endpoints below...
