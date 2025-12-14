import streamlit as st
import pandas as pd

home_page = st.Page("home_page.py", title="Home")
data_preparation_page = st.Page("data_preparation_page.py", title="Data Preparation")
model_training_and_testing_page = st.Page("model_training_and_testing_page.py", title="Model Training and Testing")
model_evaluation_page = st.Page("model_evaluation_page.py", title="Model Evalutaion")

pg = st.navigation([home_page, data_preparation_page, model_training_and_testing_page, model_evaluation_page])
pg.run()