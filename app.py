import streamlit as st


# site settings
st.set_page_config(layout="wide")

# sidebar settings
with st.sidebar.expander(label='Overview'):
  statistics = st.checkbox('General statistics', on_change=lambda: (if statistics is True: visualizations := False)[-1])
  visualizations = st.checkbox('General visualizations', on_change=lambda: (if visualizations is True: statistics := False)[-1])
  
with st.sidebar.expander(label='Search'):
  st.slider("SiO\u2082 concentration, mol%",
                  min_value = 50.0,
                  max_value = 100.0,
                  key='x1')

  st.slider("Al\u2082O\u2083 concentration, mol%",
                  min_value = 0.0,
                  max_value = 50.0,
                  key='x2')

  st.slider("Na\u2082O concentration, mol%",
                  min_value = 0.0,
                  max_value = 50.0,
                  key='x3')

  st.slider("K\u2082O concentration, mol%",
                  min_value = 0.0,
                  max_value = 50.0,
                  key='x4')

