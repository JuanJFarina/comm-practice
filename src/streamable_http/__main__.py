from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
import time
from typing import Generator
import uvicorn

app = FastAPI()


async def fake_stream():
    for i in range(10):
        time.sleep(1)
        print(f"data chunk {i}\n")
        yield f"data chunk {i}\n".encode()


@app.get("/stream")
def stream():
    return StreamingResponse(fake_stream())


if __name__ == "__main__":
    uvicorn.run(app, port=5000, log_level="info")
