import logging
from .rule_based_masking import RuleBasedMasking
from .language_detection import LanguageDetector
from .ner_masking.english import EnglishNER
from .ner_masking.german import GermanNER

class TextTransformer:
    def __init__(self) -> None:
        self.rule_masker = RuleBasedMasking()
        self.language_detector = LanguageDetector()
        # Initialize NER models for supported languages with their type annotations
        self.ner_models = {
            'en': EnglishNER(),
            'de': GermanNER(),
        }

    def transform_text(self, text: str, language: str|None = None) -> str:
        # Check if language is provided, otherwise detect it
        if not language:
            language = self.language_detector.detect_language(text)
            logging.info(f"Detected language: {language}")
        else:
            logging.info(f"Using provided language: {language}")

        # Apply rule-based masking
        text = self.rule_masker.mask_numbers(text)
        text = self.rule_masker.mask_emails(text)
        text = self.rule_masker.mask_dates(text)

        # Apply NER-based masking if model exists for the provided or detected language
        if language in self.ner_models:
            ner_model = self.ner_models[language]
            text = ner_model.mask_entities(text)
        else:
            logging.warning(f"No NER model available for language: {language}")

        return text


if __name__ == "__main__":
    transformer = TextTransformer()
    sample_texts = [
        "John Doe's email is john.doe@example.com and his phone number is 555-1234.",
        "Angela Merkel war Bundeskanzlerin von Deutschland.",
        # Add more sample texts in different languages as needed
    ]

    for text in sample_texts:
        transformed_text = transformer.transform_text(text)
        print(f"Original: {text}\nTransformed: {transformed_text}\n")
