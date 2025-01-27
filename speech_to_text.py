# # from google.cloud import speech
# # import os
# # import io

# # # Set Google credentials
# # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'aqarchain-406708-fac1abcb0b45.json'

# # # Create client instance
# # client = speech.SpeechClient()

# # # Path of your audio file
# # file_name = "/Users/muazzam/Downloads/Mere Rashke Qamar (Remix)- Baadshaho 320 Kbps.mp3"
# # with io.open(file_name, "rb") as audio_file:
# #     content = audio_file.read()
# #     audio = speech.RecognitionAudio(content=content)

# # # Config with MP3 encoding
# # config = speech.RecognitionConfig(
# #     encoding=speech.RecognitionConfig.AudioEncoding.MP3,  # Use MP3 encoding
# #     enable_automatic_punctuation=True,
# #     audio_channel_count=2,
# #     language_code="en-US"
# # )

# # # Send the request to Google to transcribe the audio
# # response = client.recognize(request={"config": config, "audio": audio})

# # # Read the response
# # for result in response.results:
# #     print("Transcript: {}".format(result.alternatives[0].transcript))


# import os
# from openai import OpenAI
# from dotenv import load_dotenv
# import streamlit as st
# load_dotenv()
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def transcribe_audio(uploaded_file):
#     """Transcribes an uploaded audio file using OpenAI Whisper."""
#     transcription = client.audio.transcriptions.create(
#         model="whisper-1",
#         file=uploaded_file
#     )
    
#     # Inspect the transcription object
#     # st.write(f"Transcription object: {transcription}")
#     # st.write(f"Attributes: {dir(transcription)}")

#     # Try to access the text attribute properly
#     try:
#         return transcription.text  # if it's an object with a text attribute
#     except AttributeError:
#         st.error("Unable to extract text from transcription object.")
#         return None



import os
from openai import OpenAI
from langdetect import detect
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def transcribe_audio(uploaded_file):
    """Transcribes audio and detects the language."""
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=uploaded_file
    )
    transcribed_text = transcription.text

    detected_language_code = detect(transcribed_text)
    
    return transcribed_text, detected_language_code
