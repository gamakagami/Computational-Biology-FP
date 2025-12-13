import streamlit as st
import pandas as pd

home_page = st.Page("home_page.py", title="Home Page")
data_preparation_page = st.Page("data_preparation_page.py", title="Data Preparation Page")
model_evaluation_page = st.Page("model_evaluation_page.py", title="Model Evalutaion Page")

pg = st.navigation([home_page, data_preparation_page, model_evaluation_page])
pg.run()