import streamlit as st

st.header("Model Evaluation")

st.markdown("#### 1. **XGBRegressor Results**")

xgb_data = {
    "Applicability Domain": [
        "None", "LeverageApplicabilityDomain", "TopKatApplicabilityDomain", "KNNApplicabilityDomain",
        "None", "LeverageApplicabilityDomain", "TopKatApplicabilityDomain", "KNNApplicabilityDomain",
        "None", "LeverageApplicabilityDomain", "TopKatApplicabilityDomain", "KNNApplicabilityDomain"
    ],
    "R2": [
        0.7304286597, 0.7121338, 0.7100745623, 0.7310280526,
        0.692611166, 0.6976595436, 0.6921120605, 0.7007859926,
        0.6735134555, 0.6808745279, 0.6762833623, 0.6864715015
    ],
    "MSE": [
        0.3508058762, 0.3542246791, 0.3550528198, 0.3330459267,
        0.4000195611, 0.3512123461, 0.3494847763, 0.3408065229,
        0.4248723109, 0.3671792779, 0.3665176271, 0.3518753665
    ],
    "MAE": [
        0.4049802726, 0.4071388077, 0.4074099717, 0.3960191414,
        0.4233281478, 0.4063513882, 0.4066848992, 0.4010369464,
        0.4296267167, 0.4110516407, 0.410518873, 0.4030771809
    ],
    "Filter": [
        "None", "None", "None", "None",
        "Z_Score Outliers Removal", "Z_Score Outliers Removal", "Z_Score Outliers Removal", "Z_Score Outliers Removal",
        "IQR Outliers Removal", "IQR Outliers Removal", "IQR Outliers Removal", "IQR Outliers Removal"
    ]
}

st.dataframe(xgb_data, height=457)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("#### 2. **Random Forest Regressor Results**")

rf_data = {
    "Applicability Domain": [
        "None", "LeverageApplicabilityDomain", "TopKatApplicabilityDomain", "KNNApplicabilityDomain",
        "None", "LeverageApplicabilityDomain", "TopKatApplicabilityDomain", "KNNApplicabilityDomain",
        "None", "LeverageApplicabilityDomain", "TopKatApplicabilityDomain", "KNNApplicabilityDomain"
    ],
    "R2": [
        0.7087085817, 0.7384745664, 0.6904414844, 0.7104364051,
        0.643790583, 0.6134693105, 0.6645070264, 0.644274374,
        0.6349464831, 0.6169814648, 0.6579279796, 0.6346960977
    ],
    "MSE": [
        0.3790712362, 0.3298425883, 0.3809308142, 0.38898729,
        0.4635520841, 0.522130335, 0.3835370159, 0.4778665195,
        0.4750613277, 0.500449865, 0.3910582107, 0.4907335642
    ],
    "MAE": [
        0.4097989201, 0.3728503534, 0.4093911102, 0.4173168284,
        0.4350506197, 0.450039785, 0.411121218, 0.4435152848,
        0.4376159029, 0.4385235708, 0.4127072972, 0.4465007172
    ],
    "Filter": [
        "None", "None", "None", "None",
        "Z_Score Outliers Removal", "Z_Score Outliers Removal", "Z_Score Outliers Removal", "Z_Score Outliers Removal",
        "IQR Outliers Removal", "IQR Outliers Removal", "IQR Outliers Removal", "IQR Outliers Removal"
    ]
}

st.dataframe(rf_data, height=457)