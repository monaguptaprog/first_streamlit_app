
import streamlit
import pandas

streamlit.title('My parents new healthy dinner')

streamlit.header('Breakfast menu')
streamlit.text('Boiled Eggs')
streamlit.text('parantha')
streamlit.text('🥑🍞 Pancake ')

streamlit.header('Build your own smoothie')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
