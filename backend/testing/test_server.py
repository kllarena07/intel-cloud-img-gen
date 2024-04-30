from fastapi import FastAPI, status

app = FastAPI()

@app.get("/task")
async def task():
    return {
      "message": "Task accepted"
    }, status.HTTP_202_ACCEPTED