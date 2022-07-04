import streamlit as st


# site settings
st.set_page_config(layout="wide")

# sidebar settings
with st.sidebar.expander(label='Overview'):
  overview = st.radio(label='Select general information to present', options=('General statistics', 'General visualizations'))
  
with st.sidebar.expander(label='Search'):
  company_name = st.text_input('Name of company')
  location = st.text_input('Location')
