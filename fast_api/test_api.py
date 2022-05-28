import os

from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home():
    # Automatically converted into a json response
    return {"Hello": "World"}
    




def main():
    return

if __name__ == '__main__':
    main()
