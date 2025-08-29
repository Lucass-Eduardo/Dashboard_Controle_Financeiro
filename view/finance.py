import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu


st.title("💰 Controle de Finanças")
    
selected2 = option_menu(None, ["Resumo", "Ganhos", "Gastos"], 
    icons=['c'
    'currency-dollar','graph-up-arrow',"graph-down-arrow"], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2
    # Exemplo de dataframe inicial
data = {
    "Categoria": ["Alimentação", "Transporte", "Educação", "Lazer"],
    "Valor": [500, 300, 200, 150],
}
df = pd.DataFrame(data)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Tabela de Gastos")
    st.dataframe(df, width='stretch')

with col2:
    st.subheader("📈 Distribuição de Gastos")
    fig = px.pie(df, values="Valor", names="Categoria", title="Gastos por categoria")
    st.plotly_chart(fig, use_container_width=True)