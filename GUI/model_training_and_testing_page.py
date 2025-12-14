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

st.markdown("2. Experiment with different number of features within the RFE. The n_feature_to_select that produces the best results will be used in the hyperparameter tuning:")
st.markdown("""
    ```python
    from xgboost import XGBRegressor
    from sklearn.feature_selection import RFE
            
    xgboost_model = XGBRegressor(random_state=42)
    xgboost_rfe = RFE(estimator=xgboost_model, n_features_to_select=60)
""")

st.markdown("3. Use the RFE to transform the X_train and X_test datasets. Perform hyperparameter tuning using RandomizedSearchCV, where it will try 100 different combinations based on the param_dist given and find out which combination is best. Then, the prediction is compared to the y_test values, where evaluation metrics such as R2, MSE and MAE are recorded.")
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

    y_pred_test = best_xgb.predict(X_test_rfe)
            
    r2_test = r2_score(y_test, y_pred_test)
    mse_test = mean_squared_error(y_test, y_pred_test)
    mae_test = mean_absolute_error(y_test, y_pred_test)

    print(f"Test R2: {r2_test}")
    print(f"Test MSE: {mse_test}")
    print(f"Test MAE: {mae_test}")
""")

st.markdown("4. To view the impact of outliers within the training set, we implemented outlier removal techniques such as z-score and IQR. Then, we recorded the results using previously stated evaluation metrics:")
st.markdown("""
    ```python
    # z-score technique
    z_scores = np.abs(zscore(y_train))
    mask = (z_scores < 3)
            
    # IQR technique
    Q1 = y_train.quantile(0.25)
    Q3 = y_train.quantile(0.75)
    IQR = Q3 - Q1
    mask = (y_train >= (Q1 - 1.5 * IQR)) & (y_train <= (Q3 + 1.5 * IQR))
            
    X_train_clean = X_train[mask]
    y_train_clean = y_train[mask]

    xgboost_rfe.fit(X_train_clean, y_train_clean)
    X_train_rfe = xgboost_rfe.transform(X_train_clean)
    X_test_rfe = xgboost_rfe.transform(X_test)

    xgboost_model.fit(X_train_rfe, y_train_clean)

    y_pred_test = xgboost_model.predict(X_test_rfe)

    r2_test = r2_score(y_test, y_pred_test)
    mse_test = mean_squared_error(y_test, y_pred_test)
    mae_test = mean_absolute_error(y_test, y_pred_test)

    print(f"Test R2: {r2_test}")
    print(f"Test MSE: {mse_test}")
    print(f"Test MAE: {mae_test}")
""")

st.markdown("5. As an additional step after the evalutation, applicability domains are implemented. It defines the boundaries within which the model's predictions are considered reliable (ADs implemented include Leverage, TopKat, and KNN applicability domain). After removing 'unreliable' predictions, the results are once again evaluated:")
st.markdown("""
    ```python
    # leverage applicability domain
    ad = LeverageApplicabilityDomain()
            
    # top kat applicability domain
    ad = TopKatApplicabilityDomain()
            
    # KNN applicability domain
    ad = KNNApplicabilityDomain()
            
    ad.fit(X_train_rfe)
    inside_ad_mask = ad.contains(X_test_rfe)

    y_test_inside = y_test[inside_ad_mask]
    y_pred_inside = y_pred_test[inside_ad_mask]
            
    r2_test = r2_score(y_test_inside, y_pred_inside)
    mse_test = mean_squared_error(y_test_inside, y_pred_inside)
    mae_test = mean_absolute_error(y_test_inside, y_pred_inside)
            
    print("R2 score:", r2_test)
    print("MSE:", mse_test)
    print("MAE:", mae_test)
""")
st.markdown("Applicability domains source code: https://github.com/OlivierBeq/MLChemAD/blob/master/src/mlchemad/applicability_domains.py")