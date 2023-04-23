from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Trading APP')


fake_data = [
    {"id": 1, "name": "John Doe1", "email": "kenaa1@example.com"},
    {"id": 2, "name": "Jane Doe2", "email": "envkt"},
    {"id": 3, "name": "John Doe3", "email": "kenaa2@example.com"},
]

@app.get('/users/{user_id}')
def get_user(user_id: int):
    return [user for user in fake_data if user["id"] == user_id]

fake_trades = [
    {'id': 1, 'user_id': 1, 'price': 100, 'currency': 'BTC'},
    {'id': 2, 'user_id': 1, 'price': 200, 'currency': 'ETH'},
    {'id': 3, 'user_id': 2, 'price': 300, 'currency': 'BTC'},
    {'id': 4, 'user_id': 2, 'price': 400, 'currency': 'ETH'},
]

class Trade(BaseModel):
    id: int
    user_id: int
    price: float
    currency: str

@app.post('/trades')
def add_trade(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}