from .model import model_call
import io
from fastapi import FastAPI, UploadFile
from PIL import Image

app = FastAPI()

@app.get("/")
def root():
    return {"message": "ML model"}

@app.post("/ask")
def ask(text: str, image: UploadFile):

    content = image.file.read()
    image_read = Image.open(io.BytesIO(content))

    result = model_call(text, image_read)

    return {"answer" : result}
