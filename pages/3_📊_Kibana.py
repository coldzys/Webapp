import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Search and Visualize", layout="wide")

with st.sidebar.expander(label='Customized option', expanded=True):
  option = st.radio(
    label='Search and visualize based on Kibana', 
    options=('Kibana searching', 'Kibana visualizing')
  )
  
def customized_option(option):
  if option == 'Kibana searching':
      components.iframe(
        src='http://172.18.0.26:5601/app/r/s/spicy-proud-hospital', 
        width=1200,
        height=1600,
        scrolling=True
      )
      
  if option == 'Kibana visualizing':
    components.iframe(
      src='http://172.18.0.26:5601/app/r/s/wrong-millions-beard', 
      width=1200,
      height=1600,
      scrolling=True
    )
    
customized_option(option)

