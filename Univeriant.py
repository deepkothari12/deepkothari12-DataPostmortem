import pandas as pd
import streamlit as st
import graph
import app

def Univerient_analysis(select):
     ##Duw to circular import
    st.title("Univariate Analysis")
    st.write("Univariate Analysis is a type of data visualization where we visualize only a single variable at a time.")
    st.write(app.df[app.optionss])
    st.write("Here is the distribution of the selected variable")
    st.dataframe(select)
    graph.graphplot(pd.DataFrame(select))