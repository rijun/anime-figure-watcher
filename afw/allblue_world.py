import re
from datetime import date

from bs4 import BeautifulSoup

from website import Website


class AllblueWorld(Website):
    def __init__(self):
        super(AllblueWorld, self).__init__()

    def get_figures(self, theme):
        params_dict = {
            'p': 1,
            'o': 1,
            'n': 99,
        }
        f_param = [1517, 1543, 1145]
        if theme == 'sao':
            additional_params = [79]
        elif theme == 'dbz':
            additional_params = [140, 2003]
        else:
            additional_params = []
        f_param += additional_params
        params_dict['f'] = '|'.join([str(x) for x in f_param])

        try:
            response = self._request_page("https://www.allblue-world.de/shop/", params_dict)
        except RuntimeError:
            return

        soup = BeautifulSoup(response, 'html.parser')

        div = soup.find('div', class_='listing--container')

        # 'title', 'price', 'url', 'save_date', 'image_path', 'description'
        products = []
        for a in div.find_all('a', class_='product--title'):
            price = re.search(r'\d+,\d+', a.find_next('span', class_='price--default').text)
            d = {
                'title': a['title'],
                'url': a['href'],
                'save_date': date.today().isoformat(),
                'image_path': a.next_sibling.find_next('img')['srcset'].split(',')[0],
                'price': f"{price.group()} €",
                'description': self._get_description(a['href'])
            }
            products.append(d)

        return products

    def _get_description(self, product_url):
        try:
            response = self._request_page(product_url)
        except RuntimeError:
            return ""

        soup = BeautifulSoup(response, 'html.parser')
        div = soup.find('div', class_='product--description')
        description_content = []
        for p in div.find_all('p'):
            description_content.append(str(p))
        return "".join(description_content)
