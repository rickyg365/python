import os


"""
www.youtube.com/watch?v=3vfum74ggHE

Requirements:
- fastapi
- "uvicorn[standard]"
- python-multipart
- sqlalchemy
- jinja2
"""
from fastapi import FastAPI

app = FastAPI()


# Async VERSION
# @app.get("/")
# async def home():
#     return {"Hello": "World"}

@app.get("/")
def home():
    # Automatically converted into a json response
    return {"Hello": "World"}

# Dynamic Route
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

