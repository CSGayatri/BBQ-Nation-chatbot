# backend/api/knowledge_base.py

from fastapi import APIRouter
import json
import os
from backend.api.utils import split_into_chunks, classify_query

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../../data/knowledge_base_cleaned.json")

with open(DATA_PATH, "r") as f:
    KNOWLEDGE = json.load(f)

@router.get("/get_info")
async def get_info(query: str):
    print("[DEBUG] Received query:", query)

    category = classify_query(query)
    print(f"[DEBUG] Classified category: '{category}'")

    print(f"[DEBUG] Available categories: {list(KNOWLEDGE.keys())}")

    content = KNOWLEDGE.get(category)
    if not content:
        print("[DEBUG] No content found for category:", category)
        return {
            "message": f"Sorry, I couldn't find any information about '{query}'.",
            "category": category,
            "chunks": []
        }

    print(f"[DEBUG] Content length: {len(content)} characters")

    chunks = split_into_chunks(content, max_tokens=800)
    print(f"[DEBUG] Number of chunks created: {len(chunks)}")

    return {
        "message": chunks[0] if chunks else "Here's the information you asked for.",
        "category": category,
        "chunks": chunks
    }
