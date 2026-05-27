from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)

    return data

@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def welcome():
    return {"message": "A fully functional API to manage your patient records"}

@app.get("/view")
def view():
    data = load_data()

    return data

@app.get("/patients/{patient_id}")
def view_patients(patient_id: str = Path(..., description="ID of the patient in the DB", example="P001")):

    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")