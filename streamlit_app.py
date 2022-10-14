import streamlit
streamlit.title('My Parents new health dinner')
streamlit.header('Lunch Menu')
streamlit.text('Rice')
streamlit.text('Saambar')
streamlit.text('Potato Fry')
streamlit.text('Curd Rice')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe('my_fruit_list')
