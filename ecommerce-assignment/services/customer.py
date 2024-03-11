from fastapi import FastAPI, HTTPException
from schema.customer import CustomerCreate, customers



class customerService:

    @staticmethod
    def validate_username(payload: CustomerCreate):
        username: str = payload.username
        for customer in customers:
            if customer.username == username:
                raise HTTPException(status_code=400, detail="username already exists")
        return payload