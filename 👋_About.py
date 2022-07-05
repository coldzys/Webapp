import streamlit as st

# site settings
st.set_page_config(page_title="About", layout="wide")

with st.sidebar.expander(label='About', expanded=True):
  option = st.radio(label='Further information about', options=('Webapp', 'System'))

def about(option):
  if option == 'Webapp':
    st.title('Job webapp: Data visualization and access tool for users')
    st.markdown('''
      The tool enables users to examine and visualize career-related data statistics. In addition, the webapp   gives the opportunity to query and adjust the visualization on the interface, as well as access to advanced capabilities via Kibana.
    ''')
  if option == 'System':
    st.title('Big data system: System for gathering, storing, processing, and analyzing massive amounts of data')
    st.markdown('''
      The system provides a comprehensive sequence of procedures to adapt to the environment of big data. The system employs the newest and most effective technologies available to provide interoperability with a wide variety of data, various data gathering and processing requirements, and business-based analytical requirements.
    ''')

about(option)

