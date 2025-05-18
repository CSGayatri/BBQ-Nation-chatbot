from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from log_to_sheet import log_conversation
import uvicorn

app = FastAPI()

# 👇 Define your schema using Pydantic
class ConversationData(BaseModel):
    modality: str
    call_time: str
    phone_number: str
    call_outcome: str
    room_name: str
    booking_date: str
    booking_time: str
    number_of_guests: int
    call_summary: str

@app.post("/log-conversation")
async def log_to_sheet(data: ConversationData):
    try:
        # 👇 Pass structured data to your logging function
        log_conversation(data)
        return {"status": "success", "message": "Logged to Google Sheet"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("api_server:app", host="0.0.0.0", port=8000, reload=True)
