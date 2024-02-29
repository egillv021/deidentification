from langdetect import detect_langs, DetectorFactory

class LanguageDetector:
    def __init__(self):
        DetectorFactory.seed = 73 #Ensures reproducible results from langdetect

    def detect_language(self, text):
        """
        Detect the most probable language of the given text.

        Parameters:
        text (str): The text for which to detect the language.

        Returns:
        str: The language code for the most probable language.
        """
        try:
            possible_langs = detect_langs(text)
            # Sort the detected languages by probability in descending order
            most_probable_lang = max(possible_langs, key=lambda lang: lang.prob)
            # Return the language code of the most probable language
            return most_probable_lang.lang
        except Exception as e:
            # Handle exceptions (e.g., if text is too short or not recognized)
            raise Exception(f"Language detection failed: {e}")

if __name__ == "__main__":
    # Usage example
    detector = LanguageDetector()
    texts = [
        "Minä rakastan sinua",
        "This is some sample text.",
        "Ceci est un texte d'exemple.",
        "这是一些示例文本。",
        "Þetta er dæmi um texta."
    ]
    
    for text in texts:
        language = detector.detect_language(text)
        print(f"Detected language for '{text}': {language}")
