import os
import json
from utilities import file_tools as ft

class Config:
    def __init__(self):
        self.config_file = os.path.join(ft.get_project_dir(), 'config.json')
        self.config = json.load(self.config_file)
        self.alpha_vantage_key = self.config['alpha_vantage_api_key']

