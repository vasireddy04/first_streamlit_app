import streamlit
streamlit.title('My Mom''s Healthy menu')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text(' ๐ฅ Kale, Spinach & Rocket Smoothie')
streamlit.text(' ๐Hard-Boiled Free-Range Egg')
streamlit.text('๐ฅ๐Avocado Toast')

streamlit.header('๐๐ฅญ Build Your Own Fruit Smoothie ๐ฅ๐')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon" + fruit_choice)
# streamlit.text(fruityvice_response.json())




