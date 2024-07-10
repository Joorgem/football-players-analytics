import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏽",
    layout="wide"
)

# Seleção de ano
anos = list(range(2017, 2024))
selected_year = st.sidebar.selectbox("Selecione o Ano", anos, index=anos.index(2023))
st.session_state["selected_year"] = selected_year

df_data = st.session_state["data"]
df_data = df_data[df_data["Year"] == selected_year]

# Carregar dados de 2023 para imagens
df_data_2023 = st.session_state["data"][st.session_state["data"]["Year"] == 2023]

# Ordenar clubes em ordem alfabética
clubes = sorted(df_data["Club"].unique())
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[(df_data["Club"] == club)]

# Ordenar jogadores em ordem alfabética
players = sorted(df_players["Name"].unique())
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

# Buscar foto do jogador em 2023
player_2023 = df_data_2023[df_data_2023["Name"] == player]
if not player_2023.empty:
    player_image = player_2023["Photo"].iloc[0]
else:
    player_image = None

if player_image:
    st.image(player_image)
st.title(player_stats["Name"])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']} anos")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100} m")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f} kgs")
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")
