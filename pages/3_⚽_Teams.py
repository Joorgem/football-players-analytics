import streamlit as st

st.set_page_config(
    page_title="Teams",
    page_icon="⚽",
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

df_filtered = df_data[(df_data["Club"] == club)].set_index("Name")

# Adicionar fotos do dataframe de 2023
df_filtered["Photo"] = df_filtered.apply(
    lambda row: df_data_2023[df_data_2023["Name"] == row.name]["Photo"].iloc[0] 
    if not df_data_2023[df_data_2023["Name"] == row.name].empty else None, axis=1)

df_filtered["Flag"] = df_filtered.apply(
    lambda row: df_data_2023[df_data_2023["Name"] == row.name]["Flag"].iloc[0] 
    if not df_data_2023[df_data_2023["Name"] == row.name].empty else None, axis=1)

# Adicionar logo do clube do dataframe de 2023
club_logo = df_data_2023[df_data_2023["Club"] == club]["Club Logo"].iloc[0] if not df_data_2023[df_data_2023["Club"] == club].empty else None
if club_logo:
    st.image(club_logo)
st.markdown(f"## {club}")

# Ordenar jogadores em ordem alfabética
columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_filtered[columns].sort_index(),
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall",format = "%d" ,min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn(
                     "Weekly Wage",format = "£%f" ,min_value=0, max_value=df_filtered["Wage(£)"].max()
                     ),
                 "Photo":st.column_config.ImageColumn(),
                 "Flag": st.column_config.ImageColumn("Country"),
             })
