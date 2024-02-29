from abc import ABC, abstractmethod

class BaseNERMasking(ABC):
    def __init__(self, model_name):
        self.model_name = model_name
        self.model = self.load_model()

    @abstractmethod
    def load_model(self):
        """
        Load the NER model specific to the language.
        """
        pass

    @abstractmethod
    def mask_entities(self, text):
        """
        Process the text, identify entities and mask them accordingly.
        """
        pass

    @abstractmethod
    def create_mask(self, entity_type):
        """
        Create a mask for a specific entity type.
        """
        pass
