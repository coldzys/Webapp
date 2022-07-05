import streamlit as st
from elasticsearch import Elasticsearch
import pandas as pd

es = Elasticsearch("http://172.18.0.25:9200")

st.set_page_config(page_title="Search and Visualize", layout="wide")

with st.form(key="input-form"):
  company_name = st.text_input("Name of company").strip()
  location = st.text_input("Location of company").strip()
  job_name = st.text_input("Name of job").strip()
  job_field = st.text_input("Job field").strip()
  degree = st.text_input("Required degree").strip()
  submitted = st.form_submit_button("Submit")
if submitted:
  results = es.sql.query(body={'query': f'SELECT age, company_name, degree, experience, job_field, job_name, level, location, salary, sex, update_time, working_form FROM "job-*" WHERE company_name LIKE \'%{company_name}%\' AND location LIKE \'%{location}%\' AND job_name LIKE \'%{job_name}%\' AND job_field LIKE \'%{job_field}%\' AND degree LIKE \'%{degree}%\''})['rows']
  df = pd.DataFrame(results, columns=["age", "company_name", "degree", "experience", "job_field", "job_name", "level", "location", "salary", "sex", "update_time", "working_form"])
  st.dataframe(df)
  st.download_button("Download", df.to_json().encode("utf-8"), "results.json")

