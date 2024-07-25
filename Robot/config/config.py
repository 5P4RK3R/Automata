# config.py
import os
from dotenv import load_dotenv
from robot.api.deco import keyword

# Load environment variables from .env file in the config directory
env_path = os.path.join(os.path.dirname(__file__), '.env')

class Config:
    def __init__(self):
        print(env_path)
        load_dotenv(env_path)

    @keyword
    def get_environment_variable(self, variable_name):
        print(variable_name)
        return os.getenv(variable_name)
# from robot import run

# Run Robot Framework tests
# run('tests', exclude='*ExcludedTests*')
