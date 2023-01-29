import streamlit
import pandas

streamlit.title('First Application')
streamlit.header('Hello World')
streamlit.text('🥣 Outside it is cloudy in Troy MI')
streamlit.text('🐔 Snow has stopped')
streamlit.text('🥗 Next week Jan-30 to Feb-07 will be freezing cold')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
