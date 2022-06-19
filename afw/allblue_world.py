from bs4 import BeautifulSoup

from website import Website


class AllblueWorld(Website):
    def __init__(self):
        super(AllblueWorld, self).__init__("https://www.allblue-world.de/shop/")

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
            response = self.request_page(params_dict)
        except RuntimeError:
            return

        soup = BeautifulSoup(response, 'html.parser')

        div = soup.find('div', class_='listing--container')

        products = []
        for a in div.find_all('a', class_='product--title'):
            products.append({
                'title': a['title'],
                'link': a['href'],
                'image': a.next_sibling.find_next('img')['srcset']
            })

        return products
