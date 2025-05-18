def classify_query(query: str) -> str:
    query = query.lower()

    if any(word in query for word in ["book", "booking", "reserve", "reservation", "table"]):
        return "booking"
    if "cancel" in query or "cancellation" in query:
        return "cancellation"
    if "menu" in query or "dishes" in query:
        return "menu"
    if any(greet in query for greet in ["hi", "hello", "hii", "hey"]):
        return "greeting"
    
    return "general"



def split_into_chunks(text: str, max_tokens: int = 800):
    words = text.split()
    chunks = []
    chunk = []
    count = 0

    for word in words:
        chunk.append(word)
        count += 1
        if count >= max_tokens:
            chunks.append(" ".join(chunk))
            chunk = []
            count = 0

    if chunk:
        chunks.append(" ".join(chunk))
    return chunks
