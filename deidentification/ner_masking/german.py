import spacy
from .base_ner_masking import BaseNERMasking

class GermanNER(BaseNERMasking):
    def __init__(self):
        super().__init__("de_core_news_lg")

    def load_model(self):
        """
        Load the German NER model.
        """
        try:
            ner_model = spacy.load(self.model_name)
            ner_model.add_pipe("merge_entities")
            return ner_model
        except Exception as e:
            raise Exception(f"Failed to load the German NER model '{self.model_name}': {e}")

    def mask_entities(self, text):
        """
        Masks entities in the provided German text.
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
        Create a mask for a specific entity type for German.
        """
        entity_masks = {
            'PER': '[PERSON]',
            'ORG': '[ORGANIZATION]',
            'LOC': '[LOCATION]',
            'MISC': '[MISC]'
        }
        return entity_masks.get(entity_type, '[MASKED]')

# Usage example:
# ner = GermanNER()
# masked_text = ner.mask_entities("Angela Merkel war Bundeskanzlerin von Deutschland.")
# print(masked_text)
