VALID_STATUSES = [
    "To do",
    "Completed"
]

def is_valid_status(status)  -> bool :
    return status in VALID_STATUSES