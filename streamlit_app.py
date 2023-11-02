import streamlit
import pandas
import requests

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

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())


streamlit.header("Fruityvice Fruit Advice!")


# normalize jason
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# makes adataframe to show normalized json
streamlit.dataframe(fruityvice_normalized)
