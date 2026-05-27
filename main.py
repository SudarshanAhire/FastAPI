from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Jay Ganesh..."}

@app.get("/welcome")
def welcome():
    return {"message": "Welcome to FastAPI..."}