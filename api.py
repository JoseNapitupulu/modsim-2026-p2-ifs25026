import subprocess
import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.middleware.proxy_headers import ProxyHeadersMiddleware

app = FastAPI()

@app.get("/")
def root():
    return {"message": "OK"}

# Jalankan Streamlit sebagai subprocess
if os.getenv("STREAMLIT_RUNNING") != "true":
    os.environ["STREAMLIT_RUNNING"] = "true"
    subprocess.Popen([
        "streamlit",
        "run",
        "app.py",
        "--server.port",
        os.environ.get("PORT", "8000"),
        "--server.address",
        "0.0.0.0",
        "--server.headless",
        "true"
    ])