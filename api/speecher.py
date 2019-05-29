import spacy
import requests

nlp = spacy.load("pt")

class Speecher:
    def __init__(self, provider):
        self.imageProvider = provider 

    def extract_theme(self, sentence):
        doc = nlp(sentence)
        nouns = [token.text for token in doc if token.pos_ == "NOUN"]
        return nouns[0] if (len(nouns) > 0) else None
    
    def get_illustration_url(self, sentence):
        theme = self.extract_theme(sentence)
        illustration_url = self.imageProvider.get_image_url(theme) if theme is not None else ""
        return illustration_url
