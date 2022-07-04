import streamlit as st


# site settings
st.set_page_config(layout="wide")

# sidebar settings
with st.sidebar.expander(label='Overview'):
  overview = st.radio(label='Select general information to present', options=('General statistics', 'General visualizations'))
  
with st.sidebar.expander(label='Web search and visualize'):
  company_name = st.text_input('Company name')
  location = st.text_input('Location')
  job_name = st.text_input('Job name')

with st.sidebar.expander(label='Customized option'):
  option = st.radio(label='Search and visualize based on Kibana', options=('Kibana searching', 'Kibana visualizing'))
  
with st.sidebar.expander(label='About'):
  option = st.radio(label='Further information about', options=('Webapp', 'System'))
