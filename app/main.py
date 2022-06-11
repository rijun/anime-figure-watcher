import logging


from allblue_world import AllblueWorld


# https://www.sukipan.com/de/Anime-Figuren/anime-serien-p-z/Sword-Art-Online/?view_mode=tiled&listing_sort=&filter_id=0&listing_count=192
# https://www.nerdchandise-online.de/advanced_search_result.php?view_mode=tiled&keywords=sword+art+online&inc_subcat=1&listing_sort=&listing_count=336
def main():
    logging.basicConfig(level=logging.INFO)
    abw = AllblueWorld()
    abw_products = abw.get_figures('sao')

    with open('example.rss', 'w') as f:
        f.write(abw_rss)

if __name__ == '__main__':
    main()
