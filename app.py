import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pecas.csv")

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x,y)

st.title("Previsão de valores no mercado")
st.title("Peças do tipo A12Bx-260")
st.divider()

diametro = st.number_input("Digite o diâmetro da peça: ")
if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f'Conforme pesquisas e dados recebidos, a tendência de valor de mercado para essa peça com diâmetro de {diametro:.2f}cm atualmente é de: R$ {preco_previsto:.2f} /un.')
    st.balloons()

