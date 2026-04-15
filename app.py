import streamlit as st
from transformers import pipeline
@st.cache_resource
def loard_summarizer():
  return pipline("summmarization model="sshleifer/distrilbart-cnn-12-6")
summarizer = load_summarizer()
st.title("AI Text Summarizer")
st.write("Enetr a long text below , and get a concise summary!")
long_text=st.text_area("Enter text to summarizer:",height=200)
max_length=st.slider("Max Summary Length",min_value=50,max_value=300,value=130)
min_length=st.slider("Min Summary Length",min_value=20,max_value=100,value=30)

if st.button("Summarize"):
  if long_text.strip();
    with st.spinner("Generating summary..."):
    summary=summarizer(long_text,max_length=max_length,min_length=min_length,do_sample=False)
    sy.subheader("Sumary:")
    st.success(summary[0]['sumary_text'])
else:
  st.waring("Please enter some text to sumarize.")
