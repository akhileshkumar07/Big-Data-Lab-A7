import uvicorn
from main import app

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000, log_level="info")