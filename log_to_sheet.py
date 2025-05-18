import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

# Pydantic model for conversation data
class ConversationData(BaseModel):
    modality: str = "Chatbot"
    call_time: str = None
    phone_number: str
    call_outcome: str = "MISC."
    room_name: str = "NA"
    booking_date: str = "NA"
    booking_time: str = "NA"
    number_of_guests: int = None
    call_summary: str = "No summary available."

# Set up Google Sheets API
def setup_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("data/google_credentials.json", scope)
    client = gspread.authorize(creds)
    
    # Replace with your actual sheet name
    sheet = client.open("BBQ_Chatbot_Log").sheet1
    return sheet

# Add a new row to the sheet using Pydantic model
def log_conversation(data: ConversationData):
    sheet = setup_google_sheets()

    # Use attribute access instead of .get()
    row = [
        data.modality,
        data.call_time or datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        data.phone_number,
        data.call_outcome,
        data.room_name,
        data.booking_date,
        data.booking_time,
        str(data.number_of_guests) if data.number_of_guests is not None else "NA",
        data.call_summary,
    ]

    sheet.append_row(row)
    print("✅ Logged conversation successfully.")

# FastAPI endpoint to receive and log conversation
@app.post("/log-conversation")
async def api_log_conversation(data: ConversationData):
    try:
        log_conversation(data)
        return {"message": "Conversation logged successfully"}
    except Exception as e:
        return {"error": str(e)}

# Example standalone usage (remove or comment out when running as FastAPI app)
if __name__ == "__main__":
    sample_data = ConversationData(
        modality="Call",
        call_time="2025-05-18 15:45:00",
        phone_number="9876543210",
        call_outcome="AVAILABILITY",
        room_name="Barbeque Nation Delhi",
        booking_date="2025-05-21",
        booking_time="18:30",
        number_of_guests=4,
        call_summary="User called to check availability for 4 people at BBQ Delhi on May 21 at 6:30 PM."
    )
    log_conversation(sample_data)