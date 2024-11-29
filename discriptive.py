import pandas as pd
import streamlit as st
import app


#Discriptive Satistics
def discriptivestate(options):
    
    #st.set_page_config(layout='wide' , page_title='DataPostmartem')

    st.title("Discriptive Satistics")
    col1 , col2 = st.columns(2)
    with col1:
         st.dataframe(app.df[options])

    with col2:
        df_shape = str(app.df[options].shape)
        st.metric("DataFram Shape Accrodin to choosen Column", df_shape ) # type: ignore
    col3 , col4 = st.columns(2)
    with col3 :
        # mising values conditions 
        st.subheader("Missing values Columns Name")
        if not (app.df[options].isnull().sum()[app.df[options].isnull().sum() > 0].sort_values(ascending=False).to_dict()):
            st.write("NO missing values")
        else :
            st.write(app.df[options].isnull().sum()[app.df[options].isnull().sum() > 0].sort_values(ascending=False).to_dict())
    with col4:
        # Duplicate Valuess
        st.subheader("Total Duplicates Values In (Columns Consider all columns)")
        if app.df.duplicated().sum() > 0:
             st.write("Duplicated")
        else:
             st.write("Not")

    col5 , col6 , col7,col8 = st.columns(4)
    with col5:
        #Mean of numerical values 
        st.subheader("Mean values")
        st.dataframe(pd.DataFrame(app.df[options].mean(numeric_only=True) , columns=[ 'Mean']))
    with col6:
        #Median of numerical values 
        st.subheader("Meadian values")
        st.dataframe(pd.DataFrame(app.df[options].median(numeric_only=True) , columns=[ 'Mean']))
    with col7:
        #mode
        st.subheader("Variance")
        st.dataframe(pd.DataFrame(app.df[options].var(numeric_only=True), columns=[ 'Variance']))
    with col8:
        #standard deviation
        st.subheader("Standard Deviation")
        st.dataframe(pd.DataFrame(app.df[options].std(numeric_only=True), columns=[ 'Standard']))

    col9 , col10  = st.columns(2)
    with col9:
        st.subheader("Data Summary")
        try:
             st.dataframe(pd.DataFrame(app.df[options].describe()))
        except :
             st.write("Data Not Available")
    
    with col10:
         
        if 'input_value' not in st.session_state:
            st.session_state.input_value = 0
            
        st.subheader("how many Percentages of your data is less than or equal to specific values.") 
         # Default value

        # Function to be called when the button is clicked
        def handle_click():
            st.session_state.input_value = st.session_state.input_number
            st.write(f"Button clicked, input value is: {st.session_state.input_value}")

        # Integer input widget with session state
        st.number_input(
            "Enter an integer:",
            min_value=0,
            max_value=100,
            step=1,
            value=st.session_state.input_value,
            key="input_number"
        )


        # Button that triggers the callback function
        st.button("Submit", on_click=handle_click)

        # Display the current value from session state
        st.write(f"Current input value is: {st.session_state.input_value}")


