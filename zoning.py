def categorize_postcode(postcode):
    cleaned = postcode.replace(" ", "").upper()
    if cleaned.startswith("SW147"):
        return "West"
    elif cleaned.startswith("SW148"):
        return "East"
    else:
        return "Unknown"
