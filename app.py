import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pecas.csv")

modelo = LinearRegression()
x = df[["diametro"]]
y = df["preco"]

st.title("Previsão de valores no mercado")
st.title("Peças do tipo A12Bx-260")


