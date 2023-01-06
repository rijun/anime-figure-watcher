import logging

import requests


class Website:
    def __init__(self):
        pass

    @staticmethod
    def _request_page(url, params=None):
        params = {} if params is None else params
        r = requests.get(url, params)
        if r.status_code != 200:
            raise RuntimeError("Request failed")
        logging.info(f"Queried {r.request.url}")
        return r.text

