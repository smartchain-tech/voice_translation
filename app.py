# import streamlit as st
# from speech_to_text import transcribe_audio
# from translate import translate_text
# from text_to_speech import convert_text_to_speech

# # Streamlit App UI
# st.title("User-to-User Speech Interaction")

# # User 1 Audio Input
# st.header("User 1: Speak Now")
# uploaded_file_1 = st.file_uploader("Upload an audio file (User 1)", type=["mp3", "wav"])

# if uploaded_file_1 is not None:
#     st.write("Processing User 1's audio...")
    
#     # Transcribe User 1's speech and detect language
#     transcribed_text_1, detected_language_code_1 = transcribe_audio(uploaded_file_1)
#     st.write(f"User 1's Transcribed Text: {transcribed_text_1}")
#     st.write(f"Detected Language: {detected_language_code_1}")
    
#     # Translate User 1's text to Arabic
#     translated_text_to_arabic = translate_text(transcribed_text_1, target_language='ar')
#     st.write(f"Translated to Arabic: {translated_text_to_arabic}")
    
#     # Convert the translated Arabic text to speech for User 2
#     arabic_speech_file = convert_text_to_speech(translated_text_to_arabic, "ar")
#     st.audio(arabic_speech_file, format='audio/mp3')

# # User 2 Audio Input
# st.header("User 2: Respond Now")
# uploaded_file_2 = st.file_uploader("Upload an audio file (User 2)", type=["mp3", "wav"])

# if uploaded_file_2 is not None:
#     st.write("Processing User 2's audio...")
    
#     # Transcribe User 2's speech
#     transcribed_text_2, _ = transcribe_audio(uploaded_file_2)
#     st.write(f"User 2's Transcribed Text: {transcribed_text_2}")
    
#     # Translate User 2's text back to User 1's language
#     translated_text_to_user_1 = translate_text(transcribed_text_2, target_language=detected_language_code_1)
#     st.write(f"Translated back to User 1's language: {translated_text_to_user_1}")
    
#     # Convert the translated text to speech for User 1
#     user_1_speech_file = convert_text_to_speech(translated_text_to_user_1, detected_language_code_1)
#     st.audio(user_1_speech_file, format='audio/mp3')




import streamlit as st
from speech_to_text import transcribe_audio
from translate import translate_text
from text_to_speech import convert_text_to_speech


st.title("User-to-User Speech Interaction")


st.header("User 1: Speak Now")
uploaded_file_1 = st.file_uploader("Upload an audio file (User 1)", type=["mp3", "wav"])

if uploaded_file_1 is not None:
    st.write("Processing User 1's audio...")
    
    transcribed_text_1, detected_language_code_1 = transcribe_audio(uploaded_file_1)
    st.write(f"User 1's Transcribed Text: {transcribed_text_1}")
    st.write(f"Detected Language: {detected_language_code_1}")
    translated_text_to_arabic = translate_text(transcribed_text_1, target_language='ar')
    st.write(f"Translated to Arabic: {translated_text_to_arabic}")
    arabic_speech_file = convert_text_to_speech(translated_text_to_arabic, "ar")
    st.audio(arabic_speech_file, format='audio/mp3')

st.header("User 2: Respond Now")
uploaded_file_2 = st.file_uploader("Upload an audio file (User 2)", type=["mp3", "wav"])

if uploaded_file_2 is not None:
    st.write("Processing User 2's audio...")
    transcribed_text_2, detected_language_code_2 = transcribe_audio(uploaded_file_2)
    st.write(f"User 2's Transcribed Text: {transcribed_text_2}")
    translated_text_to_user_1 = translate_text(transcribed_text_2, target_language=detected_language_code_1)
    st.write(f"Translated back to User 1's language: {translated_text_to_user_1}")
    user_1_speech_file = convert_text_to_speech(translated_text_to_user_1, detected_language_code_1)
    st.audio(user_1_speech_file, format='audio/mp3')

