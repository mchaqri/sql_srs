import duckdb
import streamlit as st
import pandas as pd

st.write("Apli mus")

option = st.selectbox(
    'How would you like to review?',
    ('Joins', 'Group by', 'Windows function'),
    index=None,
    placeholder= "select a theme "

)

st.write('You ve selected :', option)

data = {"a": [1, 2, 3], "b": [4, 5, 7]}
df = pd.DataFrame(data)

tab1, tab2 = st.tabs(["mus", "toutou"])

with tab1:
    input_text = st.text_area(label=" saisi l'input")
    result = duckdb.query(input_text).df()
    st.write(f" voici le resultat de  {input_text}")
    st.dataframe(result)
#with tab2:
   #@ st.dataframe(df)
