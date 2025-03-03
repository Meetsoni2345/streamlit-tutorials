import streamlit as st

st.write("Hello World: Getting Bore,Hello Brother!!")
st.title("Display Title ues st.title()")
st.write("to write txt use st.write()")
st.header("to write header use st.header()")
st.subheader("to write subheader use st.subheader()")
st.text("Hey I am simple text to write simple text use st.text()")
st.markdown("[Streamlit](https://streamlit.io/)")
st.markdown("[Streamlit Cheatlit](https://cheat-sheet.streamlit.app/)")
st.success("Success!")
st.info("Information")
st.warning("This is warning")
st.error("This is error")

from PIL import Image
img=Image.open("smj.jpg")
st.image(img,width=300,caption="Satmev Jayate")

video_file = open("vid.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)

st.video("https://www.youtube.com/watch?v=2v8urSwf8TI")

audio_file = open("song.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")

st.button("Play")

st.header("Button Widgets")

if st.button("play"):
    st.text("Hello World")
    
if st.button("play2"):
    st.text("Enjoy Music")
    st.video("https://www.youtube.com/watch?v=2v8urSwf8TI")
    
if st.checkbox("Checkbox"):
    st.text("Checkbox selected")