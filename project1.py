import streamlit as st
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title="About Us",page_icon=":zap:",layout="wide")
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
lottie_coding=load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_msdmfngy.json")
st.subheader("Welcome To TECH SRUJANOTSAV  :wave:")
st.title("Inspiring creativity and curiosity through computing.")
st.write("Discovering the power of technology!!")
st.write("---")
with st.container():
    left_column, right_column=st.columns(2)
    with left_column:
        st.subheader("About The Event 🛈")
        st.write("Join us for a day of discovery and innovation at the TECH SRUJANOTSAV Computer Science Expo!")
        st.write("This annual event brings together researchers, and professionals in the field of computer science to share their knowledge and showcase the latest advancements in technology. ")
        st.write("Attendees can explore interactive exhibits, participate in hands-on workshops, and attend talks and panels featuring some of the industry's most influential figures. Whether you're a student, researcher, or professional, the TECH SRUJANOTSAV Computer Science Expo has something for everyone. ")
        st.write("Don't miss this exciting opportunity to learn, connect, and explore the world of computer science!")
        st.write("---")
        st.subheader("Our Creators :v:")
        st.write("Chinmaya Computing Club")
with right_column:
    st_lottie(lottie_coding,height=300,key="coding")




