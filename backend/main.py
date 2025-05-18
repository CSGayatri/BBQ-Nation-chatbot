from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.knowledge_base import router as kb_router
from .logging.google_sheets_logger import log_to_sheet

app = FastAPI()

# ✅ Enable CORS to allow frontend (e.g., React on port 3000) to access FastAPI backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with ["http://localhost:3000"] for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the knowledge base router with prefix '/api'
app.include_router(kb_router, prefix="/api")

@app.post("/log")
async def log_data(data: dict):
    try:
        print("Received data:", data)  # Debug: show incoming payload
        log_to_sheet(data)
        return {"status": "success", "message": "Logged successfully."}
    except Exception as e:
        print("Logging error:", str(e))  # Debug: print any error during logging
        return {"status": "error", "message": str(e)}
