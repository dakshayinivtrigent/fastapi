from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

class token(BaseModel):
    token:str

origins=[
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origin=origins,
    allow_credentials=True,
    allow_methos=["*"],
    allow_headers=["*"]
)
@app.get("/")
def get_message():
    return {"message":"Hello worlSd"}

@app.post("/get_token")
def get_chargifi_token(token:token):
   if(token.token):
       print("Token received",token)
       return JSONResponse(status_code=200,content={"message":"token received"})
   else:
       return JSONResponse(status_code=400,content={"error":"token not received"})
   