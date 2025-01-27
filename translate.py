# from googletrans import Translator

# translator = Translator()

# def translate_text(text, target_language):
#     """Translate text to the target language."""
#     translated = translator.translate(text, dest=target_language)
#     return translated.text


from deep_translator import GoogleTranslator

def translate_text(text, target_language):
    """Translate text to the target language."""
    translator = GoogleTranslator(target=target_language)
    return translator.translate(text)

