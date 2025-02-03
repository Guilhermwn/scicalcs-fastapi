import os
from dotenv import load_dotenv
from .src.main import app

load_dotenv()

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("SERVER_HOST")
    port = int(os.getenv("PORT")) 
    uvicorn.run("src.main:app", reload=True, host=host, port=port)