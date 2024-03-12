# from typing import Union

from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def root():
  # Empty commit
  return {"message": "Hello World"}
