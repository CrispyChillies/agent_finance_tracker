
from parser import extract_expense
import pandas as pd
from datetime import datetime
import os

text = input("Nhập nội dung chi tiêu (hoặc từ giọng nói): ")

data = extract_expense(text)
data["date"] = datetime.now().strftime("%Y-%m-%d")

# Ghi vào Excel
file_path = "chi_tieu.xlsx"
if os.path.exists(file_path):
    df = pd.read_excel(file_path)
else:
    df = pd.DataFrame(columns=["Ngày", "Loại chi", "Số tiền", "Ghi chú"])

new_row = {
    "Ngày": data["date"],
    "Loại chi": data["category"],
    "Số tiền": data["amount"],
    "Ghi chú": data["note"]
}

df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
df.to_excel(file_path, index=False)
print("Đã lưu chi tiêu:", new_row)
