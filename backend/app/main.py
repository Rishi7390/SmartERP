from fastapi import FastAPI

app = FastAPI(
    title="SmartERP API"
)

@app.get("/")
def home():
    return {
        "message": "SmartERP Running"
    }