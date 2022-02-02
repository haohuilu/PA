import streamlit as st
from sklearn.ensemble import RandomForestClassifier


def rf_param_selector():

    criterion = st.selectbox("criterion", ["entropy"])
    n_estimators = st.number_input("n_estimators", 10)
    max_depth = st.number_input("max_depth", 9)
    min_samples_split = st.number_input("min_samples_split", 2)
    max_features = st.selectbox("max_features", ["log2"])
    random_state = 0

    params = {
        "criterion": criterion,
        "n_estimators": n_estimators,
        "max_depth": max_depth,
        "min_samples_split": min_samples_split,
        "max_features": max_features,
        "n_jobs": -1,
        "random_state": random_state,
    }

    model = RandomForestClassifier(**params)
    return model
