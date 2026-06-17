def generate_k_value(question: str):
    words = len(question.split())

    if words <= 5:
        return 3   # simple query

    elif words <= 12:
        return 5   # normal query

    else:
        return 8   # complex query