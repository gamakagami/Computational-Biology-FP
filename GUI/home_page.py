import streamlit as st

st.header("QSAR-Based pIC50 Prediction Dashboard")
st.markdown("Computational Biology Final Project")
st.markdown("Members: Albertus Santoso, Gabriel Anderson & Rafael Anderson")

st.subheader("Project Overview")
st.markdown("""
Drug discovery is an expensive and time consuming process, where it requires years of time to identify promising drug candidates. One of the most important features of a compound's effectiveness is its potency, which is commonly measured in IC50. IC50 represents the concentration of a substance that is able to inhibit a biological process by 50%.

This project is a Machine Learning QSAR (Quantitative Structure-Activity Relationship) model that predicts pIC50 values from molecular structures.
""")

st.subheader("Problem Statement")
st.markdown("""
- Experimental IC50 measurements are expensive and slow
- IC50 values span several orders of magnitude and are non-linear
- Manual screening of thousands of compounds is impractical
""")

st.subheader("Project Goal")
st.markdown("""
To develop a robust regression model capable of accurately predicting: pIC50 = -log10(IC50 in M) by using molecular features already provided in the dataset along with molecular descriptors derived from the smiles string.
""")

st.subheader("Methodology")
st.markdown("""
1. Data Preparation
    - The data is initially cleaned, where the values that will be used are ensured to have no null records.
    - Converting the IC50 values into pIC50 values.
    - Molecular structures represented as SMILES strings are transformed into numerical features by using the rdkit MoleculeDescriptors module. 
    - These features are combined with existing molecular attributes, which will be used in the training of the machone learning models.
    - For more details, please navigate to the **Data Preparation Page** in the sidebar.

2. Model Training
    - Various regression models including Random Forest and XGBoost are used.
    - Apply Recursive Feature Elimination (RFE) to select the most relevant features based on model performance.
    - Hyperparameters are optimized using RandomizedSearchCV to improve model performance and prevent overfitting.
            
3. Model Evaluation
    - Model performance is assessed using the following metrics: R² score, Mean Squared Error (MSE), and Mean Absolute Error (MAE).
    - Predictions are visualized to analyze the accuracy and reliability of the models.
""")