def chunk_text(text, chunk_size=2000, overlap=300):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap  # overlap step

    return chunks
