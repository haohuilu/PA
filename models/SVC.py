from sklearn import svm
import streamlit as st
from sklearn.svm import SVC


def svc_param_selector():
    C = st.number_input("C", 10)
    kernel = st.selectbox("kernel", ("rbf"))
    gamma = st.selectbox("gamma", ("scale"))
    random_state = 1
    params = {"C": C, "kernel": kernel, "gamma" = gamma, "random_state": random_state}
    model = SVC(**params)
    return model