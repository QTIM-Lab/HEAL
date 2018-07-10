import yaml


def load_config(yaml_file):

    with open(yaml_file, 'r') as yam:
        return yaml.load(yam)
