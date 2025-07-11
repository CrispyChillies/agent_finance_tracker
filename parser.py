import re


def extract_expense(text):
    text = text.lower()
    amount_match = re.search(r"(\d+)[\s]?(nghìn|k|vnd)?", text)
    if amount_match:
        amount = int(amount_match.group(1))
        if amount_match.group(2) in ["k", "nghìn"]:
            amount *= 1000
    else:
        amount = 0

    # Phân loại đơn giản
    if "ăn" in text or "uống" in text:
        category = "Ăn uống"
    elif "xăng" in text or "xe" in text:
        category = "Đi lại"
    elif "mua" in text:
        category = "Mua sắm"
    elif "thuê" in text or "nhà" in text:
        category = "Thuê nhà"
    else:
        category = "Khác"

    return {"amount": amount, "category": category, "note": text}
