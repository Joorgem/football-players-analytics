import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime 

# Carregar dados de todos os anos
anos = list(range(2017, 2024))
dfs = {}
for ano in anos:
    df = pd.read_csv(f"CLEAN_FIFA{ano}_official_data.csv", index_col=0)
    df["Year"] = ano
    dfs[ano] = df

# Armazenar todos os dados na sessão
if "data" not in st.session_state:
    df_data = pd.concat(dfs.values())
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.markdown('# FIFA OFFICIAL DATASET! ⚽')
st.sidebar.markdown("Desenvolvido por [Jorge Molina](https://github.com/Joorgem)")

btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """
O conjunto de dados de jogadores de futebol de 2017 a 2023 oferece uma visão detalhada dos profissionais do esporte, abrangendo uma ampla gama de informações. Com mais de 17.000 registros, ele inclui dados demográficos, características físicas, estatísticas de desempenho, detalhes contratuais e afiliações a clubes.

Este recurso é extremamente valioso para analistas de futebol, pesquisadores e entusiastas, possibilitando a exploração de diversos aspectos do futebol. Ele permite estudar atributos individuais dos jogadores, analisar métricas de desempenho, avaliar o mercado, investigar a dinâmica dos clubes, examinar o posicionamento dos jogadores em campo e observar o desenvolvimento dos atletas ao longo do tempo.
"""
)
