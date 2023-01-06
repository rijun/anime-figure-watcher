import pathlib
from datetime import datetime
from zoneinfo import ZoneInfo

from jinja2 import Environment, PackageLoader, select_autoescape

from afw import config


class Rss:
    def __init__(self):
        self._env = Environment(
            loader=PackageLoader("afw"),
            autoescape=select_autoescape()
        )
        self._favicon_path = "Test"
        self._output_folder = pathlib.Path(config.output_dir)
        if not self._output_folder.exists():
            self._output_folder.mkdir()

    def generate_rss_file(self, shop, link, items):
        build_date = datetime.strftime(datetime.now(tz=ZoneInfo("Europe/Berlin")), "%a, %d %b %Y %H:%M:%S %z")
        template = self._env.get_template("rss.xml")
        rss_data = template.render(shop=shop,
                                   link=link,
                                   server_url=config.server_url,
                                   build_date=build_date,
                                   favicon_path=self._favicon_path,
                                   items=items)
        self._write_rss_file(shop, rss_data)

    def _write_rss_file(self, shop, rss_data):
        with open(self._output_folder / f"{shop}.xml", 'w', encoding="utf-8") as f:
            f.write(rss_data)
