import streamlit as st

st.header("Model Training and Testing")
st.markdown("Note: The code uses the XGBoost regressor model as an example, but the other models follow the same or similar flow in model training.")

st.markdown("1. Define the pIC50_m as the independent variable and every other attribute as the independent variables. Split the dataset into training and testing sets, where 80% is used for training and 20% for testing:")
st.markdown("""
    ```python
    from sklearn.model_selection import train_test_split

    X = machine_learning_df.drop(columns=["pIC50_m"])
    y = machine_learning_df["pIC50_m"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
""")

st.markdown("2. RFECV recursively eliminates the 5 least important features at a time (step=5), evaluating the model's performance on the remaining feature subset using 3-fold cross-validation (cv=KFold) and the r2 score (scoring='r2'). The goal is to find the optimal number of features, while still ensuring at least 20 features are selected:")
st.markdown("""
    ```python
    from xgboost import XGBRegressor
    from sklearn.feature_selection import RFECV
    from sklearn.model_selection import KFold
            
    xgboost_model = XGBRegressor(random_state=42)
    rfecv = RFECV(estimator=xgboost_model, step=5, cv=KFold(n_splits=3, shuffle=True, random_state=42), scoring="r2", min_features_to_select=20, n_jobs=-1)
""")

st.markdown("3. Machine Learning Model Combinations")

st.markdown("3.1. Hyperparameter-Tuned Model")
st.markdown("Use the RFECV model to transform the X_train and X_test datasets. Perform hyperparameter tuning using RandomizedSearchCV, where it will try 100 different combinations based on the param_dist given and find out which combination is best. Lastly, the model is evaluated using evaluation metrics such as R2, MSE, and MAE. Additionally, the training and testing accuracies are compared which can help in identifying overfitting or underfitting problems.")
st.markdown("""
    ```python
    from sklearn.model_selection import RandomizedSearchCV

    xgboost_rfe.fit(X_train, y_train)
    X_train_rfe = xgboost_rfe.transform(X_train)
    X_test_rfe = xgboost_rfe.transform(X_test)

    param_dist = {
        "n_estimators": [100, 200, 300, 400, 500],
        "learning_rate": [0.01, 0.03, 0.05, 0.1],
        "max_depth": [3, 4, 5, 6],
        "min_child_weight": [3, 5, 7, 10],
        "subsample": [0.7, 0.8, 0.9],
        "colsample_bytree": [0.7, 0.8, 0.9],
        "gamma": [0, 0.1, 0.2, 0.3],
        "reg_alpha": [0.01, 0.1, 0.5, 1],
        "reg_lambda": [1, 1.5, 2, 3]
    }


    random_search = RandomizedSearchCV(
        estimator=xgboost_model,
        param_distributions=param_dist,
        n_iter=100,
        scoring='r2',
        cv=3,
        verbose=1,
        n_jobs=-1,
        random_state=42
    )

    random_search.fit(X_train_rfe, y_train)

    best_xgb = random_search.best_estimator_
    print("Best parameters:", random_search.best_params_)

    y_pred_train = best_xgb.predict(X_train_rfe)
    y_pred_test = best_xgb.predict(X_test_rfe)
""")

st.markdown("3.2. Hyperparameter-Tuned Model with Training-Set Outlier Removal")
st.markdown("To view the impact of outliers within the training set, we implemented outlier removal techniques such as z-score and IQR. Then, we recorded the results using previously stated evaluation metrics:")
st.markdown("""
    ```python
    import numpy as np
    from scipy.stats import zscore
            
    # Use the set of features that was declared optimal by RFECV
    selected_features = X.columns[rfecv.support_]
    X_selected = X[selected_features]

    # z-score technique
    z_scores = np.abs(zscore(y_train))
    mask = (z_scores < 3)
            
    # IQR technique
    Q1 = y_train.quantile(0.25)
    Q3 = y_train.quantile(0.75)
    IQR = Q3 - Q1
    mask = (y_train >= (Q1 - 1.5 * IQR)) & (y_train <= (Q3 + 1.5 * IQR))
            
    # Use the set of parameters that was declared optimal by RandomSearchCV
    final_xgb = XGBRegressor(subsample=0.7, reg_lambda=1.5, reg_alpha=0.5, n_estimators=400, min_child_weight=7, max_depth=5, learning_rate=0.05, gamma=0.1, colsample_bytree=0.7, random_state=42, n_jobs=-1, tree_method="hist", eval_metric="rmse")

    final_xgb.fit(X_train_clean, y_train_clean)

    y_pred_train = final_xgb.predict(X_train_clean)
    y_pred_test = final_xgb.predict(X_test)
""")

st.markdown("3.3. Applicability Domain Analysis of Hyperparameter-Tuned Models")
st.markdown("As an additional step after the evalutation, applicability domains are implemented. It defines the boundaries within which the model's predictions are considered reliable (ADs implemented include Leverage, TopKat, and KNN applicability domain). After removing 'unreliable' predictions, the results are once again evaluated:")
st.markdown("""
    ```python
    # leverage applicability domain
    ad = LeverageApplicabilityDomain()
            
    # top kat applicability domain
    ad = TopKatApplicabilityDomain()
            
    # KNN applicability domain
    ad = KNNApplicabilityDomain()
            
    ad.fit(X_train_rfe)
    inside_ad_train = ad.contains(X_train_rfe)
    inside_ad_test = ad.contains(X_test_rfe)

    y_train_inside = y_train[inside_ad_train]
    y_pred_train_inside = y_pred_train[inside_ad_train]

    y_test_inside = y_test[inside_ad_test]
    y_pred_test_inside = y_pred_test[inside_ad_test]
""")
st.markdown("Applicability domains source code: https://github.com/OlivierBeq/MLChemAD/blob/master/src/mlchemad/applicability_domains.py")

st.markdown("4. Evaluate the training and testing accuracy of the model using the R2, MSE, and MAE metrics:")
st.markdown("""
    ```python
    from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
            
    r2_train = r2_score(y_train, y_pred_train)
    r2_test = r2_score(y_test, y_pred_test)
    mse_train = mean_squared_error(y_train, y_pred_train)
    mse_test = mean_squared_error(y_test, y_pred_test)
    mae_train = mean_absolute_error(y_train, y_pred_train)
    mae_test = mean_absolute_error(y_test, y_pred_test)

    print(f"Training R2: {r2_train}, Test R2: {r2_test}")
    print(f"Training MSE: {mse_train}, Test MSE: {mse_test}")
    print(f"Training MAE: {mae_train}, Test MAE: {mae_test}")
""")