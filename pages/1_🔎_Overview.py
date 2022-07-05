import streamlit as st
import plotly.express as px
import pandas as pd
from elasticsearch import Elasticsearch

es = Elasticsearch("http://172.18.0.25:9200")

st.set_page_config(page_title="Overview", layout="wide")

def statistic():
  st.title("Overview")
  st.markdown("General information about recruitment data")

  col1, col2, col3, col4 = st.columns(4)

  with col1:
    number_of_records = es.sql.query(body={'query': 'SELECT count(*) FROM "job-*"'})['rows'][0][0]
    st.metric('Total records', f"{number_of_records}")
    number_of_locations = es.sql.query(body={'query': 'SELECT count(DISTINCT location) FROM "job-*"'})['rows'][0][0]
    st.metric('Total locations', f"{number_of_locations}")

  with col2:
    most_recruited_age = es.sql.query(body={'query': 'SELECT age FROM "job-*" GROUP BY age ORDER BY count(*) DESC LIMIT 2'})['rows'][1][0].strip()
    st.metric('Most recruited age', f"{most_recruited_age}")
    most_expected_degree = es.sql.query(body={'query': 'SELECT degree FROM "job-*" GROUP BY degree ORDER BY count(*) DESC LIMIT 1'})['rows'][0][0].strip()
    st.metric('Most expected degree', f"{most_expected_degree}")

  with col3:
    only_recruit_men = es.sql.query(body={'query': "SELECT count(*) FROM \"job-*\" WHERE sex = 'Nam'"})['rows'][0][0]
    st.metric('Only recruit men', f"{int(only_recruit_men) / int(number_of_records) * 100:.2f} %")
    only_recruit_women = es.sql.query(body={'query': "SELECT count(*) FROM \"job-*\" WHERE sex = 'Nữ'"})['rows'][0][0]
    st.metric('Only recruit women', f"{int(only_recruit_women) / int(number_of_records) * 100:.2f} %")

  with col4:
    wf_types = es.sql.query(body={'query': "SELECT count(DISTINCT working_form) FROM \"job-*\""})['rows'][0][0]
    st.metric('Working form types', f"{wf_types}")
    most_popular_level = es.sql.query(body={'query': "SELECT level FROM \"job-*\" GROUP BY level ORDER BY count(*) DESC LIMIT 1"})['rows'][0][0]
    st.metric('Most popular level', f"{most_popular_level}")

def visualization():
  st.title("Overview")
  st.markdown("General visualization about recruitment data")
  
  col1, col2, col3 = st.columns(3)
  
  with col1:
    results = es.sql.query(body={'query': 'SELECT sex, count(*) FROM "job-*" GROUP BY sex'})['rows']
    df = pd.DataFrame(results, columns=["sex", "number of records"])
    figure = px.bar(df, x="sex", y="number of records", title="Gender chart at work");
    st.plotly_chart(figure, use_container_width=True)
    results = results = es.sql.query(body={'query': 'SELECT age, count(*) FROM "job-*" GROUP BY age ORDER BY count(*) DESC LIMIT 10'})['rows']
    df = pd.DataFrame(results, columns=["age", "number of records"])
    figure = px.bar(df, x="age", y="number of records", title="Age chart at work");
    st.plotly_chart(figure, use_container_width=True)
    
  with col2:
    results = es.sql.query(body={'query': 'SELECT salary, count(*) FROM "job-*" WHERE salary != \'\' GROUP BY salary ORDER BY count(*) DESC LIMIT 10'})['rows']
    df = pd.DataFrame(results, columns=["salary", "number of records"])
    figure = px.bar(df, x="salary", y="number of records", title="Top 10 popular salary range");
    st.plotly_chart(figure, use_container_width=True)
    results = es.sql.query(body={'query': 'SELECT experience, count(*) FROM "job-*" GROUP BY experience ORDER BY count(*) DESC LIMIT 10'})['rows']
    df = pd.DataFrame(results, columns=["experience", "number of records"])
    figure = px.bar(df, x="experience", y="number of records", title="Top 10 popular experience range");
    st.plotly_chart(figure, use_container_width=True)
    
  with col3:
    results = es.sql.query(body={'query': 'SELECT degree, count(*) FROM "job-*" GROUP BY degree ORDER BY count(*) DESC LIMIT 10'})['rows']
    df = pd.DataFrame(results, columns=["degree", "number of records"])
    figure = px.bar(df, x="degree", y="number of records", title="Degree chart at work");
    st.plotly_chart(figure, use_container_width=True)
    results = es.sql.query(body={'query': 'SELECT location, count(*) FROM "job-*" GROUP BY location ORDER BY count(*) DESC LIMIT 10'})['rows']
    df = pd.DataFrame(results, columns=["location", "number of records"])
    figure = px.bar(df, x="location", y="number of records", title="Top 10 popular location");
    st.plotly_chart(figure, use_container_width=True)
    
    
with st.sidebar.expander(label='Overview', expanded=True):
  option = st.radio(
    label='Select general information to present', 
    options=('General statistics', 'General visualizations')
  )

if option == 'General statistics':
  statistic()
if option == 'General visualizations':
  visualization()

