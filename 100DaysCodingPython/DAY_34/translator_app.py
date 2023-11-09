from googletrans import Translator

# Create a Translator object
translator = Translator()

# Define the text you want to translate
text_to_translate = input("Enter a word for translation :")

# Detect the language of the text (optional)
detected_language = translator.detect(text_to_translate).lang
print(f"Detected language: {detected_language}")

# Translate the text to another language
target_language = 'fr'  # Spanish in this case
translated_text = translator.translate(
    text_to_translate, dest=target_language).text

# Print the translated text
print(f"Translated text: {translated_text}")
