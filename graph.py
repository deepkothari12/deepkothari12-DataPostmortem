from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st
import app


def graphplot(col):
    #col = pd.DataFrame(col , columns=)
    
    data_type = col.dtypes
    if data_type == "float64" or data_type == 'float32':
       #sns.kdeplot(col)
       fig = plt.figure(figsize=(9,7))
       sns.kdeplot(app.df[col])
       st.pyplot(fig)
    elif data_type == 'O' :
        print("This column ")
    elif data_type == 'int64' or data_type == 'int32':
        print("deep")