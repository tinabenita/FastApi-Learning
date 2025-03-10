from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Form
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

# Form data, Form Models
class FormData(BaseModel):
    username: str
    password: str
    model_config = { "extra" : "forbid" }
    
@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return {"username": data.username} 

# File Upload
@app.post("/files/")
async def create_file(file: Annotated[bytes | None, File()] = None):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}

