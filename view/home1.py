import streamlit as st


# --- Página em layout wide
st.set_page_config(
    page_title="Dashboard Financeiro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# --- CSS personalizado
st.markdown("""
<style>

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

</style>
""", unsafe_allow_html=True)



# --- Container central para o dashboard
with st.container():
    st.subheader("Dashboard Financeiro")

    # --- Filtros no topo
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.text("Selecione o período")
        period = st.radio(
            "", 
            key="visibility",
            horizontal=True,
            options=["Semanal", "Mensal", "Semestral"],
            label_visibility="collapsed"
        )

    # --- Valores mockados
    valores = {
        "periodo": {
            "Semanal": [["1200R$", "1000 R$"], ["200 R$", "+20%"], ["250 R$", "-40%"], ['250 R$', "-40%"]],
            "Mensal": [["3000R$", "2000 R$"], ["4500 R$", "+40%"], ["1000 R$", "-35%"], ['500 R$', "-10%"]],
            "Semestral": [["8000R$", "10 R$"], ["20000 R$", "+60%"], ["4000 R$", "-40%"], ['3000 R$', "-20%"]],
        }
    }

    # --- KPIs em linha (caixas com métrica)
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.metric("Saldo", valores["periodo"][period][0][0], delta=valores["periodo"][period][0][1])
    with kpi2:
        st.metric("Ganhos", valores["periodo"][period][1][0], delta=valores["periodo"][period][1][1])
    with kpi3:
        st.metric("Gastos", valores["periodo"][period][2][0], delta=valores["periodo"][period][2][1])
    with kpi4:
        st.metric("Metas", valores["periodo"][period][3][0], delta=valores["periodo"][period][3][1])

    # --- Separador
    st.markdown("---")

    # --- Gráficos lado a lado
    g1, g2 = st.columns(2)
    with g1:
        st.subheader("📈 Evolução dos Ganhos")
        st.line_chart([10, 20, 30, 25, 40, 60, 80])

    with g2:
        st.subheader("📉 Gastos por Categoria")
        st.bar_chart([30, 10, 20, 15])
