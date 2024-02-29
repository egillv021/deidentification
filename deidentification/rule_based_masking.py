import re

class RuleBasedMasking:
    def __init__(self):
        self.number_pattern = re.compile(
            r"[\d\s\+\-()\[\]]{7,}|(\d{1,2}[-/]\d{1,2}[-/]\d{2,4})"
        )
        self.email_pattern = re.compile(r'[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]{1,255}\.[a-zA-Z]{2,}')

        self.date_pattern = re.compile(
            r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December) (\d{1,2}(?:st|nd|rd|th)?) \d{4}\b"
        )

    def mask_numbers(self, text):
        return self.number_pattern.sub("[NUMBERS]", text)

    def mask_emails(self, text):
        return self.email_pattern.sub("[EMAIL]", text)

    def mask_dates(self, text):
        return self.date_pattern.sub("[DATE]", text)
