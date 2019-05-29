class ImageProvider:
    def __init__(self, provider_config):
        self.config = provider_config

    def create_request(self, q=""):
        return ""

    def get_image_url(self):
        return ""