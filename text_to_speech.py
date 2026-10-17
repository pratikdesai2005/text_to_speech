import streamlit as st
from gtts import gTTS
from io import BytesIO

st.set_page_config(page_title="Text to Speech", page_icon="🔊")
st.title("🔊 Text to Speech")

text = st.text_area("Enter your text:", height=150)

languages = {
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
    "Marathi": "mr",
    "Tamil": "ta",
    "Telugu": "te",
}
lang_name = st.selectbox("Language:", list(languages.keys()))
slow = st.checkbox("Speak slowly")

# print(f"Selected language: {lang_name}, Slow: {slow}")

if st.button("Convert to Speech"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Generating audio..."):
            try:
                tts = gTTS(text=text, lang=languages[lang_name], slow=slow)
                audio = BytesIO()
                tts.write_to_fp(audio)
                audio.seek(0)

                st.audio(audio, format="audio/mp3")
                st.download_button(
                    label="Download MP3",
                    data=audio,
                    file_name="speech.wav",
                    mime="audio/mp3",
                )
            except Exception as e:
                st.error(f"Something went wrong: {e}")