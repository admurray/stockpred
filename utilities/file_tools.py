import os

@classmethod
def get_project_dir():
    return os.path.dirname(os.path.join(os.path.abspath(__file__), os.pardir))

