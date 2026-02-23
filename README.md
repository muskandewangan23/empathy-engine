# The Empathy Engine

## Overview
The Empathy Engine is an AI-powered service that converts text into emotionally expressive speech.  
It detects the sentiment of input text and dynamically adjusts speech delivery to simulate human-like emotional tone.

## Features
- Emotion detection (Positive / Negative / Neutral)
- Intensity scaling based on sentiment strength
- Dynamic speech modulation (speed + expressive styling)
- Generates playable MP3 audio output
- Simple Streamlit web interface

## Tech Stack
- Python
- VADER Sentiment Analysis
- Google Text-to-Speech (gTTS)
- Streamlit

## How to Run Locally
- pip install -r requirements.txt
- streamlit run app.py

## Design Logic
1. Input text is analyzed using VADER sentiment analyzer.
2. Compound sentiment score determines emotion category.
3. Emotion + intensity control:
   - Speech speed (slow/fast)
   - Emphasis styling
4. gTTS generates expressive audio output.

## Future Improvements
- Real pitch control using advanced TTS APIs
- More granular emotion classes
- Voice selection options
- Conversation mode
