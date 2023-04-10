import openai
import streamlit as st
import os


openai.api_key = ('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')


st.title("GPTbyNilesh")
st.write("***")


inputone = st.text_input("Type your question here")
btnone = st.button("Run")
if btnone:
    return_openai = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": inputone}],
        max_tokens = 500,
        n=1
    )
    st.title(return_openai['choices'][0]['message']['content'])
    st.write("I am working on Followup questions scripts. Thanks!")
