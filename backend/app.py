from fastapi import FastAPI
from fastapi.responses import JSONResponse

from pymongo import MongoClient

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://db:27017/")
db = client["tinycrm"]
contacts_collection = db["contacts"]


@app.get("/")
def read_root():
    return {"message": "TinyCRM API is running!"}


@app.post("/contacts/")
def add_contact(name: str, email: str):
    contact = {"name": name, "email": email}
    result = contacts_collection.insert_one(contact)

    # Attach the generated ID as a string
    contact["_id"] = str(result.inserted_id)

    return JSONResponse(content={"message": "Contact added!", "contact": contact})


@app.get("/contacts/")
def get_contacts():
    contacts = list(contacts_collection.find({}, {"_id": 0}))
    return {"contacts": contacts}
