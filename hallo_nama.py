import streamlit as st

st.header("Hallo selamat datang")
nama = st.text_input("Masukkan nama kamu: ")
enter = st.button("Enter")
if enter:
    st.success(f"Hallo {nama}")
    st.balloons()
