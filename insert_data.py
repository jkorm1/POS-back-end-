import json
from sqlalchemy.orm import Session
from pasaraeats.database import engine, SessionLocal
from pasaraeats.models import Card

def insert_data():
    db = SessionLocal()
    # Assuming data insertion logic will be handled differently since `cards_data` is not used here
    db.commit()
    db.close()

if __name__ == "__main__":
    insert_data()
