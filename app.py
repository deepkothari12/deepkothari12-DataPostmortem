import streamlit as st
import pandas as pd

import discriptive ##Discriptive state Fileeesss
import iinfrential ##Inferntial state  Fileeesss
import Univeriant  ##Univeriant state  Fileeesss


#st.set_page_config(layout='wide' , page_title='DataPostmartem')
st.sidebar.title("Data Postmartam")
#st.sidebar.title("Data Options")


uploaded_file = st.sidebar.file_uploader("Upload Only CSV files"  , key="fileuploader")
#if uploaded_file is not None :
#dataFrame = pd.DataFrame(uploaded_file)
df = pd.read_csv('titanic.csv')# type: ignore #'titanic.csv'
st.dataframe(df)

select = st.sidebar.selectbox("What do you Have to Do?", ['Discriptive Satistics' , 'Infrential Statistic' , 'Univariate Analysis'])
btn = st.sidebar.button("Kick")

options = st.multiselect("First Select Columns" , df.columns , placeholder="Choose a Columns")
st.write(options)

if btn :

    if  select == "Discriptive Satistics":
        #st.set_page_config(layout='wide' , page_title='DataPostmartem')
        discriptive.discriptivestate(options)
        st.write(options)
        print(options)
        

    elif select == "Infrential Statistic":
        iinfrential.infrentialstate(options)
        
    else:
        Univeriant.Univerient_analysis(options)
else :
    print("Click On button")



