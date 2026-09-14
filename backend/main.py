from fastapi import FastAPI

app = FastAPI(
    title="AEGIS",
    description="Autonomous Engine for Intelligent System Healing",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "system": "AEGIS",
        "status": "online",
        "message": "AEGIS Central Backend is running",
    }