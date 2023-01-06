import logging


from allblue_world import AllblueWorld
from rss import Rss


# https://www.sukipan.com/de/Anime-Figuren/anime-serien-p-z/Sword-Art-Online/?view_mode=tiled&listing_sort=&filter_id=0&listing_count=192
# https://www.nerdchandise-online.de/advanced_search_result.php?view_mode=tiled&keywords=sword+art+online&inc_subcat=1&listing_sort=&listing_count=336
def main():
    logging.basicConfig(level=logging.INFO)
    rss = Rss()

    abw = AllblueWorld()
    abw_products = abw.get_figures('sao')

    rss.generate_rss_file('allblue-world', 'https://www.allblue-world.de', abw_products)


if __name__ == '__main__':
    main()
