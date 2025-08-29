import streamlit as st

st.title("Dashboard Financeiro")

col1, col2 = st.columns(2)

with col1:
    period = st.radio(
        "Selecione o período",
        key="visibility",
        horizontal=True,
        options=["Semanal", "Mensal", "Semestral"],
    )

row = st.container(horizontal=True)

valores = {
    "periodo": {
        "Semanal": [
            ["1200R$", "1000 R$"],
            ["200 R$", "+20%"],
            ["250 R$", "-40%"],
            ["10%", "1200"],
        ],
        "Mensal": [
            ["3000R$", "2000 R$"],
            ["4500 R$", "+40%"],
            ["1000 R$", "-35%"],
            ["10%", "1200"],
        ],
        "Semestral": [
            ["8000R$", "10 R$"],
            ["20000 R$", "+60%"],
            ["4000 R$", "-40%"],
            ["10%", "1200"],
        ],
    }
}

with row:
    st.metric(
        "Saldo",
        valores["periodo"][period][0][0],
        delta=valores["periodo"][period][0][1],
        border=True,
    )
    st.metric(
        "Ganhos",
        valores["periodo"][period][1][0],
        delta=valores["periodo"][period][1][1],
        border=True,
    )
    st.metric(
        "Gastos",
        valores["periodo"][period][2][0],
        delta=valores["periodo"][period][2][1],
        border=True,
    )
    st.metric(
        "Metas",
        valores["periodo"][period][3][0],
        delta=valores["periodo"][period][3][1],
        border=True,
    )
