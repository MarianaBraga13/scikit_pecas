import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pecas.csv")
modelo = LinearRegression()

def treinar_modelo():  
    x = df[["diametro"]]
    y = df[["preco"]]
    modelo.fit(x,y)
    return y

st.write("""# Previsão de valores de Compra no mercado de ações (USD)
    Peças do tipo A12Bx-260 - Avião Ultraleve - Bimotor""")

st.date_input("")

diametro = st.number_input("Digite o diâmetro da peça: (cm)")
if diametro > 1:
        preco_previsto = modelo.predict([[diametro]])[0][0]
        st.write(f'Conforme pesquisas e dados recebidos, a tendência de valor de mercado para essa peça com diâmetro de {diametro:.2f} cm atualmente é de: $ {preco_previsto:.2f} /unid.')
        st.warning("Indicação otimista de ganhos com a ação no mercado")
        st.balloons()
        st.divider()
else:  
    st.warning("Digite um diâmetro maior que 1.0 cm")        
