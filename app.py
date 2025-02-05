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




# import streamlit as st
# from speech_to_text import transcribe_audio
# from translate import translate_text
# from text_to_speech import convert_text_to_speech


# st.title("User-to-User Speech Interaction")


# st.header("User 1: Speak Now")
# uploaded_file_1 = st.file_uploader("Upload an audio file (User 1)", type=["mp3", "wav"])

# if uploaded_file_1 is not None:
#     st.write("Processing User 1's audio...")
    
#     transcribed_text_1, detected_language_code_1 = transcribe_audio(uploaded_file_1)
#     st.write(f"User 1's Transcribed Text: {transcribed_text_1}")
#     st.write(f"Detected Language: {detected_language_code_1}")
#     translated_text_to_arabic = translate_text(transcribed_text_1, target_language='ar')
#     st.write(f"Translated to Arabic: {translated_text_to_arabic}")
#     arabic_speech_file = convert_text_to_speech(translated_text_to_arabic, "ar")
#     st.audio(arabic_speech_file, format='audio/mp3')

# st.header("User 2: Respond Now")
# uploaded_file_2 = st.file_uploader("Upload an audio file (User 2)", type=["mp3", "wav"])

# if uploaded_file_2 is not None:
#     st.write("Processing User 2's audio...")
#     transcribed_text_2, detected_language_code_2 = transcribe_audio(uploaded_file_2)
#     st.write(f"User 2's Transcribed Text: {transcribed_text_2}")
#     translated_text_to_user_1 = translate_text(transcribed_text_2, target_language=detected_language_code_1)
#  #   st.write(f"Translated back to User 1's language: {translated_text_to_user_1}")
#  #   user_1_speech_file = convert_text_to_speech(translated_text_to_user_1, detected_language_code_1)
# #    st.audio(user_1_speech_file, format='audio/mp3')






from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
import uuid
from speech_to_text import transcribe_audio
from translate import translate_text
from text_to_speech import convert_text_to_speech
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app, resources={r"/*": {"origins": ["https://voice.smartchain.consulting", "https://translate.smartchain.consulting"]}})
# Configuration for upload folders
app.config["UPLOAD_FOLDER_USER1"] = "uploads/user1"
app.config["UPLOAD_FOLDER_USER2"] = "uploads/user2"

# Ensure the upload folders exist
for folder in [app.config["UPLOAD_FOLDER_USER1"], app.config["UPLOAD_FOLDER_USER2"]]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Store User 1's language to translate User 2's response
user1_language_code = None

@app.route('/user1', methods=['POST'])
def handle_user1():
    global user1_language_code

    # Handle the audio file from the frontend
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']
    filename = secure_filename(audio_file.filename)
    unique_filename = f"user1_{uuid.uuid4()}_{filename}"  # Create a unique filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER_USER1'], unique_filename)
    audio_file.save(file_path)

    # Transcribe and detect the language of User 1
    transcribed_text, detected_language_code = transcribe_audio(file_path)
    user1_language_code = detected_language_code  # Store for User 2's response

    # Translate to Arabic
    translated_text = translate_text(transcribed_text, target_language='ar')

    # Convert the translated text to speech (Arabic)
    arabic_audio_filename = f"user1_arabic_{uuid.uuid4()}.mp3"  # Ensure a unique filename
    arabic_audio_path = os.path.join(app.config['UPLOAD_FOLDER_USER1'], arabic_audio_filename)
    convert_text_to_speech(translated_text, language_code='ar', output_file=arabic_audio_path)

    # Construct the URL for User 1 audio
    base_url = f"https://{request.host}"  # Use HTTPS here
    user1_audio_url = f"{base_url}/uploads/user1/{arabic_audio_filename}"

    # Print the response for User 1
    print("User 1's Response:")
    print({
        "arabic_audio": user1_audio_url,
        "detected_language_code": detected_language_code,
        "translated_text": translated_text
    })

    return jsonify({
        "arabic_audio": user1_audio_url,
        "detected_language_code": detected_language_code,
        "translated_text": translated_text
    })

@app.route('/user2', methods=['POST'])
def handle_user2():
    global user1_language_code

    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']
    filename = secure_filename(audio_file.filename)
    unique_filename = f"user2_{uuid.uuid4()}_{filename}"  # Create a unique filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER_USER2'], unique_filename)
    audio_file.save(file_path)

    if not user1_language_code:
        return jsonify({"error": "User 1's language is not set yet"}), 400

    # Transcribe User 2's audio
    transcribed_text, _ = transcribe_audio(file_path)

    # Translate to User 1's language
    translated_text = translate_text(transcribed_text, target_language=user1_language_code)

    # Convert translated text to speech (User 1's language)
    user1_audio_filename = f"user2_{uuid.uuid4()}.mp3"  # Ensure a unique filename
    user1_audio_path = os.path.join(app.config['UPLOAD_FOLDER_USER1'], user1_audio_filename)
    convert_text_to_speech(translated_text, language_code=user1_language_code, output_file=user1_audio_path)

    # Construct the URL for User 2 audio
    base_url = f"https://{request.host}"  # Use HTTPS for the URL
    user2_audio_url = f"{base_url}/uploads/user2/{unique_filename}"
    user1_audio_url = f"{base_url}/uploads/user1/{user1_audio_filename}"  # Create URL for User 1's audio response

    return jsonify({
        
        "translated_text": translated_text,
        "user1_language_audio": user1_audio_url,
        #"user2_audio_url": user2_audio_url
    })

@app.route('/uploads/user1/<path:filename>', methods=['GET'])
def get_user1_audio_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER_USER1'], filename)

@app.route('/uploads/user2/<path:filename>', methods=['GET'])
def get_user2_audio_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER_USER2'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3004) 

