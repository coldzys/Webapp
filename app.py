import streamlit as st


# site settings
st.set_page_config(layout="wide")

# sidebar settings
with st.sidebar.form(key='my_form'):
  st.subheader('Glass composition')

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

  submit_button = st.form_submit_button(label='Calculate!', on_click=form_callback)
  st.write("When you run the model, compositions will be rescaled to ensure they sum to 100%.")
