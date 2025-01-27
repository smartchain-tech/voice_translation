# from twilio.rest import Client

# account_sid = 'AC4f7fa6210cee28300f32a960fc309446'
# auth_token = 'd998a6f98e991e381d3204eb226efabf'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   body='Your appointment is coming up on July 21 at 3PM',
#   to='whatsapp:+971556902820'
# )

# print(message.body)


# import requests


# url = "https://app.chatwoot.com/api/v1/accounts/101882/conversations/3"
# api_access_token ="ERVcTCRYZ8EgjSAK27zSezTm"  

# headers = {
#     "api_access_token ":api_access_token,
#     "Content-Type": "application/json"
# }

# response = requests.get(url, headers=headers)

# print(response.status_code)
# print(response.json())


# import streamlit as st
# import torch
# import torchaudio
# # from transformers import Wav2Vec2ForSequenceClassification, Wav2Vec2Processor

# from transformers import Wav2Vec2Processor, Wav2Vec2ForSequenceClassification
# from pydub import AudioSegment
# import os

# APP_NAME = 'Voice Message Language Detection - Alternative'
# APP_DESCRIPTION = '<i>Model used: ' \
#                   '<a href="https://huggingface.co/facebook/wav2vec2-large-xlsr-53" ' \
#                   'target="_blank">Wav2Vec2 Large XLSR-53</a></i>'
# APP_REP = '<i> <a href="https://github.com/Dk-A-r/SoundML" target="_blank">Project repository</a></i>'

# TEMP_AUDIO_FILE = "temp.wav"

# def load_audio():
#     """Creating an Audio Upload Form"""
#     uploaded_file = st.file_uploader(label='Upload an audio file for language detection', type=['wav', 'mp3', 'ogg', 'flac', 'aac', 'm4a'])
#     if uploaded_file:
#         st.write("Audio file uploaded: ", uploaded_file.name)
#         audio_data = uploaded_file.getvalue()
#         st.write("Audio data size (bytes): ", len(audio_data))
#         st.audio(audio_data)

#         temp_audio_path = f"temp.{uploaded_file.name.split('.')[-1]}"
#         with open(temp_audio_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())

#         if not temp_audio_path.endswith(".wav"):
#             audio = AudioSegment.from_file(temp_audio_path)
#             audio.export(TEMP_AUDIO_FILE, format="wav")
#             st.write(f"Audio converted to {TEMP_AUDIO_FILE}")
#         else:
#             os.rename(temp_audio_path, TEMP_AUDIO_FILE)

#         if os.path.exists(TEMP_AUDIO_FILE):
#             st.write(f"Audio saved successfully to {TEMP_AUDIO_FILE}")
#             return True
#         else:
#             st.error(f"Failed to save audio file to {TEMP_AUDIO_FILE}")
#     else:
#         st.warning("No audio file uploaded")
#     return False

# @st.cache_resource
# def load_model():
#     processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-xlsr-53")
#     model = Wav2Vec2ForSequenceClassification.from_pretrained("facebook/wav2vec2-large-xlsr-53")
#     return processor, model
# # def load_model():
# #     processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-xlsr-53", cache_dir="./models")
# #     model = Wav2Vec2ForSequenceClassification.from_pretrained("facebook/wav2vec2-large-xlsr-53", cache_dir="./models")
# #     return processor, model

# def identify_language(processor, model):
#     try:
#         speech_array, _ = torchaudio.load(TEMP_AUDIO_FILE)
#         inputs = processor(speech_array.squeeze().numpy(), return_tensors="pt", sampling_rate=16000)
#         with torch.no_grad():
#             logits = model(**inputs).logits
#         predicted_ids = torch.argmax(logits, dim=-1).item()
#         language = model.config.id2label[predicted_ids]
#         st.write(f"Detected language: **{language}**")
#     except Exception as e:
#         st.error(f"Error identifying language: {e}")

# def main():
#     st.set_page_config(page_title=APP_NAME)
#     st.title(APP_NAME)
#     st.markdown(APP_DESCRIPTION, True)
#     st.markdown(APP_REP, True)

#     st.info('Upload a voice message, and the app will detect its language using Wav2Vec2.')

#     if load_audio():
#         result = st.button('Identify Language')
#         if result:
#             processor, model = load_model()
#             identify_language(processor, model)

# if __name__ == "__main__":
#     main()





# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# import time


# chrome_options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(options=chrome_options)

# # Open the target website
# url = "https://qr.finedinemenu.com/social-restaurant/menu/6347ccc687a9770015c133a0"
# driver.get(url)

# # Wait for the page to load completely
# time.sleep(5)

# # Extract the container element using the given XPath
# try:
#     container = driver.find_element(By.XPATH, '//*[@id="container-6347e1c4033d17001515fd12"]/div')

#     # Extract all text inside this container
#     all_text = container.text
#     print("Text content:")
#     print(all_text)

#     # Extract all images inside this container
#     images = container.find_elements(By.TAG_NAME, 'img')
    
#     print("\nImage Links:")
#     for img in images:
#         print(img.get_attribute('src'))  

# except Exception as e:
#     print(f"Error: {e}")

# # Close the browser
# driver.quit()



