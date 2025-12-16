import streamlit as st

st.header("QSAR-Based pIC50 Prediction Dashboard")
st.markdown("Computational Biology Final Project")
st.markdown("Members: Albertus Santoso, Gabriel Anderson & Rafael Anderson <br> <br>", unsafe_allow_html=True)

st.markdown("#### 1. **Why This Project Matters**")
st.markdown("""
Modern drug discovery faces a fundamental challenge: **how do we identify promising compounds quickly, accurately, and at scale?**  
Traditional wet-lab experiments, while essential, are **slow, costly, and resource-intensive**. As chemical libraries grow into the millions, computational tools become indispensable.

This dashboard demonstrates how **machine learning and cheminformatics** can accelerate early‑stage drug discovery by predicting compound potency directly from molecular structure.
""")

st.markdown("#### 2. **Project Overview**",)
st.markdown("""
This project focuses on predicting **pIC50**, a logarithmic measure of compound potency derived from IC50 values.  
Using a combination of **molecular descriptors**, **SMILES-based features**, and **machine learning models**, we build a QSAR (Quantitative Structure–Activity Relationship) system capable of estimating biological activity without laboratory experiments.
""")

st.markdown("#### 3. **Problem Statement**")
st.markdown("""
- Experimental IC50 measurements are expensive and slow  
- IC50 values span several orders of magnitude and are non-linear  
- Manual screening of thousands of compounds is impractical  
- Early-stage filtering requires fast, scalable computational tools  
""")

st.markdown("#### 4. **Project Goal**")
st.markdown("""
To develop a robust regression model capable of accurately predicting:

**pIC50 = -log10(IC50 in M)**

using:
- Molecular features from the dataset  
- RDKit-generated molecular descriptors  
- Machine learning models optimized for QSAR tasks  
""")

st.markdown("#### 5. **What You Can Do in This Dashboard**")
st.markdown("""
This interactive dashboard allows you to:

✅ Explore how molecular data is processed  
✅ Understand how descriptors are generated  
✅ Compare machine learning models   
✅ Learn how QSAR models support drug discovery  

Each page in the sidebar walks you through a different stage of the pipeline.
""")

st.markdown("#### 6. **Real-World Applications**")
st.markdown("""
QSAR-based pIC50 prediction is widely used in:

- **Virtual screening** of large chemical libraries  
- **Lead optimization** in medicinal chemistry  
- **Toxicity and ADMET prediction**  
- **Reducing experimental workload** in early drug discovery  

By predicting potency computationally, researchers can focus lab resources on the most promising candidates.
""")

st.markdown("#### 7. **How to Navigate This Dashboard**")
st.markdown("""
- **Home Page** — Overview of the project and its importance  
- **Data Preparation Page** — How raw data becomes ML-ready  
- **Model Training and Testing Page** — Machine learning model training, optimization, and evaluation workflow
- **Model Evaluation Page** — Performance metrics and visualizations  

Use the sidebar to move between sections.
""")

