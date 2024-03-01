import spacy
from .base_ner_masking import BaseNERMasking

class EnglishNER(BaseNERMasking):
    def __init__(self):
        super().__init__("en_core_web_trf")

    def load_model(self):
        """
        Load the English NER model.
        """
        try:
            ner_model = spacy.load(self.model_name)
            ner_model.add_pipe("merge_entities")
            return ner_model
        except Exception as e:
            raise Exception(f"Failed to load the NER model '{self.model_name}': {e}")

    def mask_entities(self, text):
        """
        Masks entities in the provided English text.
        """
        doc = self.model(text)
        masked_text = []
        for ent in doc.ents:
            mask = self.create_mask(ent.label_)
            masked_text.append(text[:ent.start_char] + mask + text[ent.end_char:])
            text = text[ent.end_char:]
        # Add any remaining text after the last entity
        masked_text.append(text)
        return "".join(masked_text)

    def create_mask(self, entity_type):
        """
        Create a mask for a specific entity type for English.
        """
        entity_masks = {
            'PERSON': '[PERSON]',
            'NORP': '[GROUP]',
            'FAC': '[FACILITY]',
            'ORG': '[ORGANIZATION]',
            'GPE': '[COUNTRY]',
            'LOC': '[LOCATION]',
            'PRODUCT': '[PRODUCT]',
            'EVENT': '[EVENT]',
            'WORK_OF_ART': '[ARTWORK]',
            'LAW': '[LAW]',
            'LANGUAGE': '[LANGUAGE]',
            'DATE': '[DATE]',
            'TIME': '[TIME]',
            'PERCENT': '[PERCENT]',
            'MONEY': '[MONEY]',
            'QUANTITY': '[QUANTITY]',
            'ORDINAL': '[ORDINAL]',
            'CARDINAL': '[NUMBER]',
        }
        return entity_masks.get(entity_type, '[MASKED]')

# Usage example:
# ner = EnglishNER()
# masked_text = ner.mask_entities("Steve Jobs founded Apple in Cupertino.")
# print(masked_text)