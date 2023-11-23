import streamlit as st
import re

def transform_linebreaks_into_spaces(text):
    textWithSpaces = text.replace('\n', ' ')
    return re.sub(r'\s+', ' ', textWithSpaces)

def doubleQuotes_to_SingleQuotes(text):
    return text.replace('"', "'")

st.set_page_config(page_title="Multiline")

st.title("Transform multiline texts into texts with just one line")
st.write("Use this app to convert a text with multiple lines (like a SQL query) into a text with just one line")

multilineText = st.text_input("Insert the multiline text")

if multilineText:
    if st.button("Transform!"):
        oneLineText = transform_linebreaks_into_spaces(doubleQuotes_to_SingleQuotes(multilineText)).strip()
        st.write("**Your text in just one line!**")
        st.write(multilineText)
        Text = f'''{multilineText}'''

        st.write("**Your option to copy to clipboard!**")
        st.code(Text, language="python")

