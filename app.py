import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

# ======================
# Configurações iniciais
# ======================
st.set_page_config(page_title="Dashboard Financeiro", layout="wide")

# ======================
# Sidebar com Menu
# ======================
with st.sidebar:
    selected = option_menu(
        "",
        ["Principal", "Finanças", "Metas", "Edição"],
        icons=["house", "wallet", "clipboard2-data", "calculator"],
        menu_icon="cast",
        default_index=0,
        styles={
            "icon": {"color": "white", "font-size": "25px"},
        }
    )

# ======================
# Página Principal
# ======================
if selected == "Principal":
    st.title("🏠 Página Principal")
    selected3 = option_menu(None, ["Home", "Upload", 'Settings'], 
        icons=['house', 'cloud-upload','gear'], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#e8f2fc"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#182c44"},
        }
    )
    st.write("Bem-vindo ao seu **Dashboard Financeiro Pessoal** 🚀")
    st.info("Use o menu ao lado para navegar entre as seções.")

# ======================
# Página Finanças
# ======================
elif selected == "Finanças":
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
        st.dataframe(df, use_container_width=True)

    with col2:
        st.subheader("📈 Distribuição de Gastos")
        fig = px.pie(df, values="Valor", names="Categoria", title="Gastos por categoria")
        st.plotly_chart(fig, use_container_width=True)

# ======================
# Página Metas
# ======================
elif selected == "Metas":
    st.title("🎯 Definição de Metas")

    meta = st.number_input("Defina sua meta de economia mensal (R$):", min_value=0, step=100)
    gasto_atual = 950  # exemplo fixo
    st.metric("Meta de Economia", f"R$ {meta}", f"-{gasto_atual - meta} de diferença")

# ======================
# Página Edição
# ======================
elif selected == "Edição":
    st.title("📝 Edição de Dados")

    categoria = st.text_input("Nome da categoria")
    valor = st.number_input("Valor gasto", min_value=0, step=10)

    if st.button("Adicionar"):
        st.success(f"Categoria **{categoria}** adicionada com valor **R$ {valor}** ✅")
