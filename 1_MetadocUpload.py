import streamlit as st
import pandas as pd
from io import StringIO

st.title("Metadoc File Upload" )
# st.button("Upload",type="primary",on_click="C://");
upload_file = st.file_uploader("Choose a file",type='csv')
if upload_file is not None:
    # databyte = upload_file.getvalue()
    # iostrings = StringIO(upload_file.getvalue().decode("utf-8"))
    # string_data = iostrings.read()
    df = pd.read_csv(upload_file)
    st.dataframe(df, use_container_width=True)
    #
    # uploaded_file = st.file_uploader("Upload a CSV file", type='csv')
    # if uploaded_file is not None:
    #     data = pd.read_csv(uploaded_file)
    #     st.write(data)

    st.title("Metadoc File Filter" )

    multiselect = st.multiselect("Select Metadoc filter columns", options=df.columns[0:], max_selections=200)
    selected_columns = df[multiselect]
    # print(selected_columns)
    st.write(selected_columns)



