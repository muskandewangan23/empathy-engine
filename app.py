
import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from gtts import gTTS
import os

analyzer = SentimentIntensityAnalyzer()

def detect_emotion(text):
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.3:
        emotion = "positive"
    elif compound <= -0.3:
        emotion = "negative"
    else:
        emotion = "neutral"

    intensity = abs(compound)
    return emotion, intensity, scores

def apply_voice_style(text, emotion, intensity):

    if emotion == "positive":
        slow = False
        prefix = "😊 "
    elif emotion == "negative":
        slow = True
        prefix = "I understand. "
    else:
        slow = False
        prefix = ""

    if intensity > 0.7:
        text = text.upper()
    elif intensity > 0.4:
        text = text + "..."

    styled_text = prefix + text
    return styled_text, slow

def speak_with_empathy(text, filename="output.mp3"):
    emotion, intensity, scores = detect_emotion(text)
    styled_text, slow = apply_voice_style(text, emotion, intensity)

    tts = gTTS(styled_text, lang="en", slow=slow)
    tts.save(filename)

    return emotion, intensity, filename


st.title("🎙️ The Empathy Engine")
st.write("Enter text and hear emotionally expressive AI speech.")

text = st.text_area("Enter your message:")

if st.button("Generate Speech"):
    if text.strip():
        emotion, intensity, file = speak_with_empathy(text)

        st.success(f"Detected Emotion: {emotion} | Intensity: {round(intensity,2)}")

        audio_file = open(file, "rb")
        st.audio(audio_file.read(), format="audio/mp3")
    else:
        st.warning("Please enter some text.")
