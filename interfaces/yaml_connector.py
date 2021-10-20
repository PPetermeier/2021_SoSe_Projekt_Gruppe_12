import yaml


def einkaeufe(path):
    try:
        with open(path) as file:
            yamlfile = yaml.load(file, Loader=yaml.FullLoader)
        listoflists = []
        for key in yamlfile.keys():
            listoflists.append(key)
        return listoflists
    except (RuntimeError, TypeError, NameError):
        pass


def listenelemente(path):
    try:
        with open(path) as fh:
            data = yaml.safe_load(fh)
            print(data)
        return data
    except (RuntimeError, TypeError, NameError):
        pass


def yaml_output(path, data):
    try:
        with open(path, 'w') as outfile:  # Dictionary zurück in YAML schreiben
            yaml.dump(data, outfile, default_flow_style=False)
            return 1
    except (RuntimeError, TypeError, NameError):
        return 0
        pass

