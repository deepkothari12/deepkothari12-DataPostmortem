import streamlit as st

# Initialize session state for the integer input if it doesn't exist
if 'input_value' not in st.session_state:
    st.session_state.input_value = 0  # Default value

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
