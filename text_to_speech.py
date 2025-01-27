# # import os
# # from google.cloud import texttospeech
# # from test import transcribed_text
# # CREDENTIALS_PATH = "/Users/muazzam/Desktop/Twilio/aqarchain-406708-fac1abcb0b45.json"
# # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS_PATH

# # client=texttospeech.TextToSpeechClient()

# # # text_block="""
# # # مرحبا كيف حالك ماذا يحدث أو في كل مكان
# # # """
# # text_block=transcribed_text
# # synthesis_input=texttospeech.SynthesisInput(text=text_block)

# # voice=texttospeech.VoiceSelectionParams(
# # language_code="ar-001",
# # name='ar-XA-Standard-C'

# # )
# # audio_config=texttospeech.AudioConfig(
# #     audio_encoding=texttospeech.AudioEncoding.MP3,
# #     effects_profile_id=['small-bluetooth-speaker-class-device'],
# #     speaking_rate=0.9,
# #     pitch=1
# # )

# # response=client.synthesize_speech(
# #     input=synthesis_input,
# #     voice=voice,
# #     audio_config=audio_config 
# # )
# # with open("output.mp3","wb") as output:
# #     output.write(response.audio_content)
# #     print("Audio Cotent in Output.mp3")


# import os
# from google.cloud import texttospeech
# from dotenv import load_dotenv

# load_dotenv()

# # Ensure Google Cloud credentials are set
# CREDENTIALS_PATH = "aqarchain-406708-fac1abcb0b45.json"
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS_PATH

# client = texttospeech.TextToSpeechClient()

# def convert_text_to_speech(text, output_file="output.mp3"):
#     """Converts text to speech in Arabic using Google Cloud's TTS."""
#     synthesis_input = texttospeech.SynthesisInput(text=text)

#     voice = texttospeech.VoiceSelectionParams(
#         language_code="ar-001",
#         name='ar-XA-Standard-C'
#     )
    
#     audio_config = texttospeech.AudioConfig(
#         audio_encoding=texttospeech.AudioEncoding.MP3,
#         effects_profile_id=['small-bluetooth-speaker-class-device'],
#         speaking_rate=0.9,
#         pitch=1
#     )

#     response = client.synthesize_speech(
#         input=synthesis_input,
#         voice=voice,
#         audio_config=audio_config
#     )

#     # Save the audio content to the specified file
#     with open(output_file, "wb") as output:
#         output.write(response.audio_content)

#     return output_file



# import os
# from google.cloud import texttospeech
# from dotenv import load_dotenv

# load_dotenv()
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "aqarchain-406708-fac1abcb0b45.json"
# client = texttospeech.TextToSpeechClient()

# def convert_text_to_speech(text, language_code, output_file="output.mp3"):
#     """Converts text to speech in the specified language."""
#     synthesis_input = texttospeech.SynthesisInput(text=text)

#     voice = texttospeech.VoiceSelectionParams(
#         language_code=language_code,
#         name="ar-XA-Wavenet-B"
#     )

	
    
#     audio_config = texttospeech.AudioConfig(
#         audio_encoding=texttospeech.AudioEncoding.MP3,
#         effects_profile_id=['small-bluetooth-speaker-class-device'],
#         speaking_rate=0.9,
#         pitch=1
#     )

#     response = client.synthesize_speech(
#         input=synthesis_input,
#         voice=voice,
#         audio_config=audio_config
#     )

#     with open(output_file, "wb") as output:
#         output.write(response.audio_content)
    
#     return output_file



import os
from google.cloud import texttospeech
from dotenv import load_dotenv

load_dotenv()

# Ensure Google Cloud credentials are set
# CREDENTIALS_PATH = ""
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ="aqarchain-406708-fac1abcb0b45.json"

client = texttospeech.TextToSpeechClient()

def get_voice_parameters(language_code):
    """Return voice parameters based on language code."""

    voice_params= {
    "en": {
        "language_code": "en-US",
        "name": "en-US-Wavenet-D"  
    },
    "es": {
        "language_code": "es-ES",
        "name": "es-ES-Wavenet-C"  
    },
    "fr": {
        "language_code": "fr-FR",
        "name": "fr-FR-Wavenet-A"  
    },
    "de": {
        "language_code": "de-DE",
        "name": "de-DE-Wavenet-B"  
    },
    "it": {
        "language_code": "it-IT",
        "name": "it-IT-Wavenet-A"  
    },
    "pt": {
        "language_code": "pt-BR",
        "name": "pt-BR-Wavenet-A"  
    },
    "zh": {
        "language_code": "cmn-Hans-CN",
        "name": "cmn-Hans-CN-Wavenet-A"  
    },
    "ja": {
        "language_code": "ja-JP",
        "name": "ja-JP-Wavenet-C"  
    },
    "ko": {
        "language_code": "ko-KR",
        "name": "ko-KR-Wavenet-D"  
    },
    "ar": {
        "language_code": "ar-001",
        "name": "ar-XA-Wavenet-B"  
    },
    "ru": {
        "language_code": "ru-RU",
        "name": "ru-RU-Wavenet-B"  
    },
    "hi": {
        "language_code": "hi-IN",
        "name": "hi-IN-Wavenet-A"  
    },
    "tr": {
        "language_code": "tr-TR",
        "name": "tr-TR-Wavenet-B"  
    },
    "nl": {
        "language_code": "nl-NL",
        "name": "nl-NL-Wavenet-C"  
    },
    "sv": {
        "language_code": "sv-SE",
        "name": "sv-SE-Wavenet-A"  
    },
    "no": {
        "language_code": "no-NO",
        "name": "no-NO-Wavenet-A"  
    },
      "ur": {
        "language_code": "ur-IN",  
        "name": "ur-IN-Wavenet-B" 
    },
    "ms":{
        "language_code":"ms-MY",
         "name": "ms-MY-Standard-B"
},
    "id":{
    "language_code":"id-ID",
    "name": "id-ID-Wavenet-B"
},
    "bn":{
   "language_code":"bn-IN",
   "name":"bn-IN-Standard-D"
},
   "fa": {
        "language_code": "fa-IR", 
        "name": "fa-IR-Wavenet-A"  
    }
}

  
    return voice_params.get(language_code, voice_params["en"])

def convert_text_to_speech(text, language_code, output_file="output.mp3"):
    """Converts text to speech in the specified language."""
    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice_params = get_voice_parameters(language_code)
    voice = texttospeech.VoiceSelectionParams(
        language_code=voice_params["language_code"],
        name=voice_params["name"]
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        effects_profile_id=['small-bluetooth-speaker-class-device'],
        speaking_rate=0.9,
        pitch=1
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    # Save the audio content to the specified file
    with open(output_file, "wb") as output:
        output.write(response.audio_content)

    return output_file
