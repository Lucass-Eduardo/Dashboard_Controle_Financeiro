import streamlit as st
import pandas as pd
import numpy as np

# --- Configuração da página
st.set_page_config(
    page_title="Dashboard Financeiro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS personalizado
st.markdown("""
<style>
/* Fundo e espaçamento do container principal */
.css-18e3th9 {
    padding-top: 2rem;
    padding-right: 3rem;
    padding-left: 3rem;
    padding-bottom: 2rem;
    background-color: #f8f9fa;
}

/* Título principal */
h1 {
    font-size: 1rem;
    font-weight: 100;
    margin-bottom: 1rem;
}

/* Cards de métricas */
.stMetric {
    background: transparent;
    border-radius: 15px;
    padding: 1rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

/* Gráficos e containers */
.block-container {
    background: transparent;
    padding: 2rem 1rem 1rem 1rem;
    border-radius: 15px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# --- Container central
with st.container():
    st.subheader("Resumo Financeiro")

    # --- Filtros no topo
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        period = st.radio(
            "Selecione o período", 
            key="visibility",
            horizontal=True,
            options=["Semanal", "Mensal", "Semestral"],
            label_visibility="collapsed"
        )

    # --- Valores mockados
    valores = {
        "periodo": {
            "Semanal": [["R$5.850,00", "+R$150"], ["R$8.000,00", "+R$200"], ["R$2.150,00", "-R$50"], ['76%', '5000']],
            "Mensal": [["R$15.000,00", "+R$500"], ["R$20.000,00", "+R$400"], ["R$5.000,00", "-R$300"], ['85%', '50000']],
            "Semestral": [["R$50.000,00", "+R$2000"], ["R$80.000,00", "+R$4000"], ["R$20.000,00", "-R$1000"], ['90%', '5000']],
        }
    }

    # --- KPIs em linha (cards)
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.metric("Saldo", valores["periodo"][period][0][0], delta=valores["periodo"][period][0][1])
    with kpi2:
        st.metric("Ganhos", valores["periodo"][period][1][0], delta=valores["periodo"][period][1][1])
    with kpi3:
        st.metric("Gastos", valores["periodo"][period][2][0], delta=valores["periodo"][period][2][1])
    with kpi4:
        st.metric("% Meta", valores["periodo"][period][3][0],delta=valores["periodo"][period][3][1])

    st.markdown("---")

    # --- Gráficos lado a lado
    g1, g2 = st.columns([3, 2])
    with g1:
        st.subheader("Evolução")
        st.line_chart(np.random.randint(1000, 4000, size=(7, 2)), use_container_width=True)

    with g2:
        st.subheader("Gastos por categoria")
        st.bar_chart(np.random.randint(200, 800, size=(4,)), use_container_width=True)
