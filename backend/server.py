from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fabric import Connection
from dotenv import dotenv_values
from pydantic import BaseModel

config = dotenv_values(".env")

HOST_IP = config["HOST_IP"]
GATEWAY_IP = config["GATEWAY_IP"]
SSH_KEY = config["SSH_KEY"]

playground = Connection(host=HOST_IP,
                        gateway=Connection(GATEWAY_IP),
                        connect_kwargs={
                          "key_filename": [SSH_KEY]
                        })

app = FastAPI()

origins = [
  "http://127.0.0.1:3000",
  "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello_world")
def hello_world():
    """This function is purely for testing if the connection worked."""
    result = playground.run("python3 test.py")
    return {
      "message": result.stdout,
      "status_code": 200
    }

@app.get("/learn_coding")
def learn_coding():
    """LLM Inferencing Test. Passing in quieres is not supported."""
    result = playground.run("cd ~/intro-to-hf && python3 inference.py")
    split = result.stdout.split("Result: ")
    return {
      "message": split[1],
      "status_code": 200
    }

@app.get("/gojo")
def gojo():
    """Transfering an image from remote to the server."""
    playground.get("/home/ubuntu/images.jpeg")

    return FileResponse("images.jpeg", media_type="image/jpeg")

class UserPrompt(BaseModel):
    prompt: str

@app.post("/generate/")
def generate_image(args: UserPrompt):
    playground.run(f"python3 inference.py --prompt '{args.prompt}'")
    playground.get("/home/ubuntu/inference.jpeg")

    return FileResponse("inference.jpeg", media_type="image/jpeg")
