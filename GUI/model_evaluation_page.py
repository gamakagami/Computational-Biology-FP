import streamlit as st

st.header("Model Evaluation")

st.markdown("#### 1. **XGBRegressor Results**")

xgb_data = {
    "Applicability Domain": [
        "None", "LeverageApplicabilityDomain", "TopKatApplicabilityDomain", "KNNApplicabilityDomain",
        "None", "LeverageApplicabilityDomain", "TopKatApplicabilityDomain", "KNNApplicabilityDomain",
        "None", "LeverageApplicabilityDomain", "TopKatApplicabilityDomain", "KNNApplicabilityDomain"
    ],
    "Train R2": [
        0.804, 0.798, 0.785, 0.800,
        0.781, 0.776, 0.772, 0.775,
        0.783, 0.778, 0.774, 0.777
    ],
    "Train MSE": [
        0.262, 0.263, 0.264, 0.262,
        0.255, 0.256, 0.256, 0.255,
        0.247, 0.248, 0.248, 0.246
    ],
    "Train MAE": [
        0.384, 0.386, 0.387, 0.384,
        0.380, 0.381, 0.381, 0.380,
        0.376, 0.377, 0.377, 0.375
    ],
    "Test R2": [
        0.694, 0.680, 0.664, 0.696,
        0.667, 0.659, 0.655, 0.669,
        0.665, 0.659, 0.652, 0.672
    ],
    "Test MSE": [
        0.398, 0.401, 0.403, 0.374,
        0.434, 0.396, 0.397, 0.373,
        0.436, 0.396, 0.397, 0.369
    ],
    "Test MAE": [
        0.461, 0.464, 0.465, 0.452,
        0.472, 0.396, 0.459, 0.448,
        0.471, 0.459, 0.458, 0.445
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
        "None", "TopKatApplicabilityDomain", "KNNApplicabilityDomain",
        "None", "TopKatApplicabilityDomain", "KNNApplicabilityDomain",
        "None", "TopKatApplicabilityDomain", "KNNApplicabilityDomain"
    ],
    "Train R2": [
        0.891, 0.889, 0.891,
        0.878, 0.877, 0.877,
        0.879, 0.878, 0.878
    ],
    "Train MSE": [
        0.146, 0.142, 0.149,
        0.143, 0.138, 0.146,
        0.138, 0.134, 0.141
    ],
    "Train MAE": [
        0.249, 0.245, 0.252,
        0.243, 0.244, 0.252,
        0.247, 0.243, 0.250
    ],
    "Test R2": [
        0.707, 0.694, 0.708,
        0.644, 0.667, 0.644,
        0.630, 0.661, 0.629
    ],
    "Test MSE": [
        0.382, 0.377, 0.392,
        0.463, 0.419, 0.478,
        0.482, 0.389, 0.498
    ],
    "Test MAE": [
        0.421, 0.416, 0.427,
        0.446, 0.419, 0.454,
        0.450, 0.421, 0.458
    ],
    "Filter": [
        "None", "None", "None",
        "Z_Score Outliers Removal", "Z_Score Outliers Removal", "Z_Score Outliers Removal",
        "IQR Outliers Removal", "IQR Outliers Removal", "IQR Outliers Removal"
    ]
}

st.dataframe(rf_data, height=352)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("#### 3. **Catboost Regressor Results**")

cat_data = {
    "Applicability Domain": [
        "None", "LeverageApplicabilityDomain", "TopKatApplicabilityDomain", "KNNApplicabilityDomain",
        "None", "LeverageApplicabilityDomain", "TopKatApplicabilityDomain", "KNNApplicabilityDomain",
        "None", "LeverageApplicabilityDomain", "TopKatApplicabilityDomain", "KNNApplicabilityDomain"
    ],
    "Train R2": [
        0.835, 0.813, 0.824, 0.836,
        0.820, 0.813, 0.812, 0.821,
        0.822, 0.815, 0.814, 0.823
    ],
    "Train MSE": [
        0.221, 0.225, 0.222, 0.224,
        0.210, 0.213, 0.210, 0.213,
        0.202, 0.204, 0.203, 0.205
    ],
    "Train MAE": [
        0.352, 0.356, 0.353, 0.354,
        0.343, 0.348, 0.344, 0.345,
        0.338, 0.338, 0.338, 0.340
    ],
    "Test R2": [
        0.703, 0.688, 0.685, 0.706,
        0.658, 0.640, 0.665, 0.659,
        0.652, 0.675, 0.662, 0.654
    ],
    "Test MSE": [
        0.387, 0.394, 0.386, 0.395,
        0.445, 0.487, 0.382, 0.458,
        0.453, 0.380, 0.386, 0.465
    ],
    "Test MAE": [
        0.451, 0.446, 0.449, 0.455,
        0.468, 0.481, 0.448, 0.474,
        0.467, 0.437, 0.386, 0.473
    ],
    "Filter": [
        "None", "None", "None", "None",
        "Z_Score Outliers Removal", "Z_Score Outliers Removal", "Z_Score Outliers Removal", "Z_Score Outliers Removal",
        "IQR Outliers Removal", "IQR Outliers Removal", "IQR Outliers Removal", "IQR Outliers Removal"
    ]
}

st.dataframe(cat_data, height=457)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("#### 4. **ANN Results**")

ann_data = {
    "Applicability Domain": [
        "None", "TopKatApplicabilityDomain", "KNNApplicabilityDomain",
        "None", "TopKatApplicabilityDomain", "KNNApplicabilityDomain",
        "None", "TopKatApplicabilityDomain", "KNNApplicabilityDomain"
    ],
    "Train R2": [
        0.770, 0.758, 0.772,
        0.743, 0.731, 0.745,
        0.723, 0.713, 0.727
    ],
    "Train MSE": [
        0.309, 0.307, 0.312,
        0.300, 0.302, 0.303,
        0.315, 0.315, 0.316
    ],
    "Train MAE": [
        0.403, 0.404, 0.405,
        0.399, 0.401, 0.401,
        0.415, 0.417, 0.415
    ],
    "Test R2": [
        0.653, 0.653, 0.656,
        0.622, 0.621, 0.625,
        0.618, 0.614, 0.621
    ],
    "Test MSE": [
        0.451, 0.427, 0.462,
        0.491, 0.435, 0.503,
        0.497, 0.443, 0.510
    ],
    "Test MAE": [
        0.483, 0.471, 0.488,
        0.502, 0.477, 0.506,
        0.514, 0.493, 0.520
    ],
    "Filter": [
        "None", "None", "None",
        "Z_Score Outliers Removal", "Z_Score Outliers Removal", "Z_Score Outliers Removal",
        "IQR Outliers Removal", "IQR Outliers Removal", "IQR Outliers Removal"
    ]
}

st.dataframe(ann_data, height=352)