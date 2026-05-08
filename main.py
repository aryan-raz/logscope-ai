from fastapi import FastAPI

app = FastAPI(
    title="Log Analysis Engine",
    version="1.0.0"
)

@app.get("/")
def health():
    return {
        "status": "running"
    }