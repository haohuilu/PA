from sklearn import svm
import streamlit as st
from sklearn.svm import SVC


def svc_param_selector():
    C = st.number_input("C", 10, 2.0, 1.0, 0.01)
    kernel = st.selectbox("kernel", ("rbf", "linear", "poly", "sigmoid"))
    random_state = 1
    params = {"C": C, "kernel": kernel, "random_state": random_state}
    model = SVC(**params)
    return model