import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def log_to_sheet(data: dict):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("data/google_credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("BBQ_Chat_Logs").sheet1

    row = [
        data.get("modality", ""),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        data.get("phone_number", ""),
        data.get("call_outcome", ""),
        data.get("room_name", ""),
        data.get("booking_date", ""),
        data.get("booking_time", ""),
        data.get("number_of_guests", ""),
        data.get("call_summary", "")
    ]
    sheet.append_row(row)
