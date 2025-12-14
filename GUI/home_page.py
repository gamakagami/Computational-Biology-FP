import streamlit as st

st.header("QSAR-Based pIC50 Prediction Dashboard")
st.markdown("Computational Biology Final Project")
st.markdown("Members: Albertus Santoso, Gabriel Anderson & Rafael Anderson")

# -----------------------------
# INTRODUCTION
# -----------------------------
st.subheader("Why This Project Matters")
st.markdown("""
Modern drug discovery faces a fundamental challenge: **how do we identify promising compounds quickly, accurately, and at scale?**  
Traditional wet-lab experiments, while essential, are **slow, costly, and resource-intensive**. As chemical libraries grow into the millions, computational tools become indispensable.

This dashboard demonstrates how **machine learning and cheminformatics** can accelerate early‑stage drug discovery by predicting compound potency directly from molecular structure.
""")

# -----------------------------
# PROJECT OVERVIEW
# -----------------------------
st.subheader("Project Overview")
st.markdown("""
This project focuses on predicting **pIC50**, a logarithmic measure of compound potency derived from IC50 values.  
Using a combination of **molecular descriptors**, **SMILES-based features**, and **machine learning models**, we build a QSAR (Quantitative Structure–Activity Relationship) system capable of estimating biological activity without laboratory experiments.
""")

# -----------------------------
# PROBLEM STATEMENT
# -----------------------------
st.subheader("Problem Statement")
st.markdown("""
- Experimental IC50 measurements are expensive and slow  
- IC50 values span several orders of magnitude and are non-linear  
- Manual screening of thousands of compounds is impractical  
- Early-stage filtering requires fast, scalable computational tools  
""")

# -----------------------------
# PROJECT GOAL
# -----------------------------
st.subheader("Project Goal")
st.markdown("""
To develop a robust regression model capable of accurately predicting:

**pIC50 = -log10(IC50 in M)**

using:
- Molecular features from the dataset  
- RDKit-generated molecular descriptors  
- Machine learning models optimized for QSAR tasks  
""")

# -----------------------------
# METHODOLOGY
# -----------------------------
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

# -----------------------------
# NEW SECTION: WHAT THIS DASHBOARD OFFERS
# -----------------------------
st.subheader("What You Can Do in This Dashboard")
st.markdown("""
This interactive dashboard allows you to:

✅ Explore how molecular data is processed  
✅ Understand how descriptors are generated  
✅ Compare machine learning models  
✅ Visualize prediction performance  
✅ Learn how QSAR models support drug discovery  

Each page in the sidebar walks you through a different stage of the pipeline.
""")

# -----------------------------
# NEW SECTION: IMPACT & APPLICATIONS
# -----------------------------
st.subheader("Real-World Applications")
st.markdown("""
QSAR-based pIC50 prediction is widely used in:

- **Virtual screening** of large chemical libraries  
- **Lead optimization** in medicinal chemistry  
- **Toxicity and ADMET prediction**  
- **Reducing experimental workload** in early drug discovery  

By predicting potency computationally, researchers can focus lab resources on the most promising candidates.
""")

# -----------------------------
# NEW SECTION: HOW TO NAVIGATE
# -----------------------------
st.subheader("How to Navigate This Dashboard")
st.markdown("""
- **Home Page** — Overview of the project and its importance  
- **Data Preparation Page** — How raw data becomes ML-ready  
- **Model Evaluation Page** — Performance metrics and visualizations  

Use the sidebar to move between sections.
""")
