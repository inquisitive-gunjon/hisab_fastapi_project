from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def read_something():
    return {"message": "Hello I am Gunjon Roy"}