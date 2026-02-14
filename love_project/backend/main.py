from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()

SECRET_PASSWORD = "foreverlove"

class LoginData(BaseModel):
    password: str

@app.post("/login")
def login(data: LoginData):
    if data.password == SECRET_PASSWORD:
        return {"status": "success"}
    return {"status": "failed"}

@app.get("/counters")
def counters():
    today = date.today()
    marriage = date(2024, 11, 17)
    reception = date(2024, 11, 16)
    husband_bday = date(1998, 12, 2)
    son_bday = date(2025, 10, 23)

    days_married = (today - marriage).days

    return {
        "days_married": days_married
    }
