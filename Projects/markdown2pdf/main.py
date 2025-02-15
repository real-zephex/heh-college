from fastapi import FastAPI
import uvicorn as uv
from src.index import convert
import base64

app = FastAPI()

@app.get("/")
def welcome():
    return {
        "message": "PDF API is working properly",
        "version": 1.0
    }

@app.get("/pdf/{content}")
def pdf(content: str):
    print(content)
    decoded = base64.b64decode(content).decode("utf-8")
    convert(str(decoded))
    return decoded

if __name__ == "__main__":
    uv.run(app, port=6969)