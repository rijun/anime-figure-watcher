import logging

import requests


class Website:
    def __init__(self, url):
        self.url = url

    def request_page(self, params):
        r = requests.get(self.url, params)
        if r.status_code != 200:
            raise RuntimeError("Request failed")
        logging.info(f"Queried {r.request.url}")
        return r.text

