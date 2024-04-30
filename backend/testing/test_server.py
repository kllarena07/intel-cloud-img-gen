from fastapi import FastAPI, status
import asyncio

app = FastAPI()

async def simulate_background_task():
    await asyncio.sleep(5)
    return {"result": "Task completed!"}

@app.get("/task")
async def task():
    return {
      "message": "Task accepted"
    }, status.HTTP_202_ACCEPTED