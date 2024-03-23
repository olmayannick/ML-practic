
import streamlit as st
import pandas as pd
import pickle



st.title("Maaş tahmin:heavy_dollar_sign:")

model = pickle.load(open("model.pkl", "rb"))
tecrube = st.number_input("Tecrube",1,10)
yazili = st.number_input("Yazılı",1,10)
mulakat = st.number_input("Mulakat",1,10)

if st.button("tahmin et"):
    tahmin = model.predict([[tecrube, yazili, mulakat]])
    tahmin = round(tahmin[0],2)
    st.write(f"Tahmin edeilen maas: {tahmin}")