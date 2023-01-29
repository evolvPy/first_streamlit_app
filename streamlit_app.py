import streamlit
import pandas

streamlit.title('First Application')
streamlit.header('Hello World')
streamlit.text('🥣 Outside it is cloudy in Troy MI')
streamlit.text('🐔 Snow has stopped')
streamlit.text('🥗 Next week Jan-30 to Feb-07 will be freezing cold')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
