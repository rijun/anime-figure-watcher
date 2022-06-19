import configparser


class Configuration:
    def __init__(self, config_file_path='config.ini'):
        self._cp = configparser.ConfigParser()
        self._cp.read_file(open(config_file_path))
        if not self._validate_configuration():
            exit(1)
        self.server_url = self._cp['general']['server_url']
        self.output_dir = self._cp['general']['output_dir']

    def _validate_configuration(self):
        if 'general' not in self._cp.sections():
            print("[general] section missing")
            return False

        expected_general_settings = {
            'server_url',
            'output_dir'
        }

        settings_diff = expected_general_settings - set(self._cp['general'])

        if settings_diff:
            print(f"Settings {settings_diff} missing")
            return False
        else:
            return True
