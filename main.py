from fastapi import FastAPI

app = FastAPI(title='Trading APP')


fake_data = [
    {"id": 1, "name": "John Doe1", "email": "kenaa1@example.com"},
    {"id": 2, "name": "Jane Doe2", "email": "envkt"},
    {"id": 3, "name": "John Doe3", "email": "kenaa2@example.com"},
]

@app.get('/')
def hello():
    return {"message": "Hello World"}

