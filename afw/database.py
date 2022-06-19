import pathlib
import sqlite3


class Database:
    def __init__(self):
        database_file = pathlib.Path('db.sqlite')
        database_setup_required = not database_file.exists()
        self._con = sqlite3.connect(database_file)
        if database_setup_required:
            self._setup_database()

    def __del__(self):
        logging.info("Closing database")
        self._con.close()

    def _setup_database(self):
        with self._con:
            self._con.execute("CREATE TABLE items (shop text, title text, url text, save_date text, image_path text, description text, price real)")
