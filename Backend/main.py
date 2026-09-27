# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Union
import server_logic

app = FastAPI(title="RPC Web Service - Sistem Terdistribusi")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model untuk input angka (Math)
class MathRequest(BaseModel):
    a: float
    b: float

# Model untuk input teks
class TextRequest(BaseModel):
    teks: str

# Model untuk input list
class ListRequest(BaseModel):
    item: Union[str, int]
    data_list: list

@app.post("/api/tambah")
def rpc_tambah(req: MathRequest):
    return {"hasil": server_logic.tambah(req.a, req.b)}

@app.post("/api/kali")
def rpc_kali(req: MathRequest):
    return {"hasil": server_logic.kali(req.a, req.b)}

@app.post("/api/pangkat")
def rpc_pangkat(req: MathRequest):
    return {"hasil": server_logic.pangkat(req.a, req.b)}

@app.post("/api/balik-teks")
def rpc_balik_teks(req: TextRequest):
    return {"hasil": server_logic.balik_teks(req.teks)}

@app.post("/api/append-data")
def rpc_append(req: ListRequest):
    return {"hasil": server_logic.append_data(req.item, req.data_list)}