import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Theo dõi chi tiêu", layout="wide")
st.title("📊 Theo dõi chi tiêu cá nhân")

if not os.path.exists("chi_tieu.xlsx"):
    st.warning("Chưa có dữ liệu chi tiêu.")
else:
    df = pd.read_excel("chi_tieu.xlsx")
    df["Ngày"] = pd.to_datetime(df["Ngày"])

    # Tổng chi
    st.metric("Tổng chi", f"{df['Số tiền'].sum():,.0f} VND")

    # Chi theo loại
    by_cat = df.groupby("Loại chi")["Số tiền"].sum()
    st.bar_chart(by_cat)

    # Lọc theo tháng
    df["Tháng"] = df["Ngày"].dt.to_period("M")
    month = st.selectbox("Chọn tháng", sorted(df["Tháng"].unique().astype(str)))
    month_data = df[df["Tháng"] == month]

    st.subheader(f"Chi tiết tháng {month}")
    st.dataframe(month_data[["Ngày", "Loại chi", "Số tiền", "Ghi chú"]])
