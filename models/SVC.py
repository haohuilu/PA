from sklearn import svm
import streamlit as st
from sklearn.svm import SVC


def svc_param_selector():
    C = st.number_input("C", 10)
    kernel = st.selectbox("kernel", ("rbf"))
    gamme = st.selectbox("gamma", ("scale"))
    params = {"C": C, "kernel": kernel, "gamma" = gamma}
    model = SVC(**params)
    return model