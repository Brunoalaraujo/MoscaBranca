from fastapi import FastAPI

import requests
import json

app = FastAPI()

@app.get("/teste/")
def helloworld():
    return {"Hello": "World"}