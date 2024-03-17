from fastapi import FastAPI, HTTPException
from uuid import uuid4
from database import SessionLocal, engine, Base
from models import InputData, SessionResult

app = FastAPI()

@app.post("/sync_sum/")
async def sync_sum(data: InputData):
    try:
        total_sum = sum(int(num) for num in data.array if num is not None)
        return {"result": total_sum}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid input data")

@app.post("/async_sum/")
async def async_sum(data: InputData):
    session_id = str(uuid4())
    total_sum = sum(int(num) for num in data.array if num is not None)
    db = SessionLocal()
    db.execute("INSERT INTO sessions (session_id, total_sum) VALUES (:session_id, :total_sum)",
               {"session_id": session_id, "total_sum": total_sum})
    db.commit()
    
    return {"session_id": session_id}

@app.get("/result/{session_id}")
async def get_result(session_id: str):
    db = SessionLocal()
    result = db.execute("SELECT total_sum FROM sessions WHERE session_id = :session_id",
                        {"session_id": session_id}).fetchone()
    
    if result is None:
        raise HTTPException(status_code=404, detail="Session not found")
    
    return {"result": result[0]}

Base.metadata.create_all(bind=engine)