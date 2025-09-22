import uvicorn
from fastapi import FastAPI, Request
from datetime import datetime, UTC
import os

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI via Nginx"}

@app.post("/raw")
async def receive_raw(request: Request):
    body = await request.body()   # retrieve raw data (bytes)
    os.makedirs("uploads", exist_ok=True)
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    filename = f"uploads/{timestamp}.bin"
    with open(filename, "wb") as f:
        f.write(body)
    
    return {
        "length": len(body),
        "preview": body[:100].decode(errors="ignore"), 
        "saved": filename,
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)  
