import requests
from image_provider import ImageProvider

class PixabayImageProvider(ImageProvider):
    def __init__(self, config):
        print('Config', config)
        self.config = config

    def create_request(self, q):
        url = self.config.url
        order = self.config.order
        page = self.config.page
        per_page = self.config.per_page
        api_key = self.config.key
        parameters = "?key={0}&q={1}&page={2}&per_page={3}&order={4}".format(api_key, q, page, per_page, order)
        pixabay_url = "{0}/{1}".format(url, parameters)
        return pixabay_url

    def get_image_url(self, term):
        pixabay_url = self.create_request(term)
        print('Url: ', pixabay_url)
        r = requests.get(pixabay_url)
        if (r.status_code == 200):
            json_data = r.json()
            hits = json_data["hits"]
            first_image = hits[0] if len(hits) > 0 else None
            url = first_image["webformatURL"]
            return url
        else:
            raise Exception('An error has ocurred. Unable to get image format', r.text())    
