import pandas as pd
import streamlit as st
import streamlit_controllerDF as sc

# Recommended layout
st.set_page_config(page_title="Controller DF",
    page_icon="tv.png", layout="wide")
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# END Layout


placeholder = st.empty()
with st.expander('Upload File'):
    uploaded_file = placeholder.file_uploader("Choose a file")
if uploaded_file:
    placeholder.empty()
    df = pd.read_csv(uploaded_file)
    ctrldf = sc.Widgets(df, omit_columns=[])
    st.dataframe(ctrldf.show(), use_container_width=True)
    ctrldf.metrics()
