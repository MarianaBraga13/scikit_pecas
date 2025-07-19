import matplotlib.pyplot as plt
import numpy as np
from app import preco_previsto
import pandas as pd
import streamlit as plt

df = pd.read_csv("pecas.csv")

def gerar_grafico(modelo):
    x_vals = np.linspace(df["diametro"].min(), df["diametro"].max(), 200).reshape(-1, 1)
    y_preds = modelo.predict(x_vals)

    # Gera valores para a reta
x_vals = np.linspace(df["diametro"].min(), df["diametro"].max(), 100).reshape(-1, 1)
y_preds = modelo.predict(x_vals)

# Cria o gráfico
fig, ax = plt.subplots()
ax.scatter(df["diametro"], df["preco"], color="blue", label="Dados reais")
ax.plot(x_vals, y_preds, color="red", label="Reta de regressão")

# Adiciona o ponto previsto em verde (se o usuário já digitou algo)
if diametro > 1:
    ax.scatter([diametro], [preco_previsto], color="green", s=100, label="Previsão atual")

ax.set_xlabel("Diâmetro (cm)")
ax.set_ylabel("Preço ($)")
ax.set_title("Previsão de Preço vs Diâmetro da Peça")
ax.legend()
ax.grid(True)

# Exibe no Streamlit
st.pyplot(fig)
