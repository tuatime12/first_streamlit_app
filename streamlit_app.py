import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')

#change 

streamlit.header('Breakfast Favs')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avacado Toast')

 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#import all packages, create a Pandas DF

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)


my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page
streamlit.dataframe(fruits_to_show)


#create API to get fruityvice data


#streamlit.text(fruityvice_response.json())


streamlit.header("Fruityvice Fruit Advice!")


try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
       streamlit.error("Please select a fruit to get more information.")
   else:
       fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
       fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
       streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()



# choose fruit
streamlit.write('The user entered ', fruit_choice)


# normalize jason
# makes adataframe to show normalized json



## Query Trial Account data in Snowflake


Streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

#add fruit:

fruit_add = streamlit.text_input('What fruit would you like to add?')
streamlit.write('thanks for adding ', fruit_add)


my_cur.execute("insert into fruit_load_list values ('from streamlit')")
