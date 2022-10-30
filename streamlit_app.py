import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Parents new health dinner')
streamlit.header('Lunch Menu')
streamlit.text('Rice')
streamlit.text('Saambar')
streamlit.text('Potato Fry')
streamlit.text('Curd Rice')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)
my_fruit_list=my_fruit_list.set_index('Fruit')

#Let's put a pick list here so they can pick the fruit they want to include
fruits_selected=streamlit.multiselect("Pick Some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#my_fruit_list=my_fruit_list.set_index('Fruit')
#streamlit.dataframe(my_fruit_list)

#create repeatale code lock(function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
#New section to display Fruitvice API response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_fuction=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_fuction)
    streamlit.write('The user entered ', fruit_choice)
   
    #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    #streamlit.text(fruityvice_response.json())--just write the data to screen
except URLError as e:
  streamlit.error()
  
# Normalize the json response
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Output in table format
#streamlit.dataframe(fruityvice_normalized)
#don't run anything past here while we troubleshoot

streamlit.header("The fruit load list contains:")
#sowflake related functions
def get_friut_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
#add autton to load fruit
if streamlit.button('Get frut load list')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows = get_fruit_load_list()
#streamlit.text("The fruit load list contains:")
#streamlit.text(my_data_row)
streamlit.dataframe(my_data_rows)
streamlit.stop()


#Another section to display Fruitvice API response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response.json())--just write the data to screen

# Normalize the json response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Output in table format
streamlit.dataframe(fruityvice_normalized)
