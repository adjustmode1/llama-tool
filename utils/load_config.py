import yaml
import os 

def load_config(config_file):
    with open(os.path.join(os.getcwd(), config_file), 'r') as file:
        config = yaml.safe_load(file)
    return config