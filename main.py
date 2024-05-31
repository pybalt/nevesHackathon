from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from foresight.router import router as foresight_api
from rpcnode.router import router as rpcnode_api

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(foresight_api, prefix="/foresight", tags=["foresight"])
app.include_router(rpcnode_api, prefix="/rpcnode", tags=["rpcnode"])
