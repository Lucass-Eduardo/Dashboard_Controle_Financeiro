import streamlit as st

paginas = [
    st.Page("view/home.py"),
    st.Page("view/home1.py"),
    st.Page("view/home2.py"),
    st.Page("view/home3.py"),
    st.Page("view/home4.py"),
    st.Page("view/home5.py"),
    st.Page("view/home6.py"),
    st.Page("view/finance.py"),
]

pg = st.navigation(paginas)

# O passo final é chamar a função run() na página selecionada.
# O Streamlit cuidará de executar o script da página correta.
pg.run()