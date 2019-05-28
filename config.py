import json
import os

class SpeecherConfiguration:
    """Represents a set of speecher configurations"""

    def __init__(self, url, key, page, per_page, order):
        self.url = url
        self.key = key
        self.page = page
        self.per_page = per_page
        self.order = order

    def __str__(self):
        order = self.order
        page = self.page
        per_page = self.per_page
        key = self.key
        parameters = "?key={0}&page={1}per_page={2}&order={3}".format(key, page, per_page, order)
        pixabay_url = "https://pixabay.com/api/{0}".format(parameters)
        return pixabay_url

def load_configuration(self, config_path="dev.json"):
    """Load configuration from a <env>.json file"""
    with open(config_path) as config_file:
        jsonData = json.load(config_file)
        config = SpeecherConfiguration(
            jsonData["pixabayUrl"],
            jsonData["pixabayApiKey"],
            jsonData["pixabayPage"],
            jsonData["pixabayPerPage"],
            jsonData["pixabayOrder"],
        )

    return config