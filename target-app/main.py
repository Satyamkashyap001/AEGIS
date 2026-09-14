from fastapi import FastAPI

app = FastAPI(
    title="AEGIS Target Application",
    description="Demo application monitored by AEGIS",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "application": "AEGIS Target Application",
        "status": "healthy",
        "message": "Target application is running",
    }
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }