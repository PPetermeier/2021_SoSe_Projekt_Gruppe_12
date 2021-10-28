import yaml



def tester():
    with open("../save_data/admin_grocery.yaml") as f:
        yamltester = yaml.safe_load(f)


def liste_entfernen(path, liste):

    yamlfile = None

    try:
        with open(path) as file:
            yamlfile = yaml.safe_load(file)
            for l in yamlfile:
                if l == liste:
                    del yamlfile[liste]
    except:
        pass

    yaml_output(path, yamlfile)

def einkaeufe(path, archiviert):
    try:
        with open(path) as file:
            yamlfile = yaml.load(file, Loader=yaml.FullLoader)
        listoflists = []

        for key, value in yamlfile.items():

            if value[0]['archiviert'] == archiviert:
                listoflists.append(key)

        return listoflists

    except (RuntimeError, TypeError, NameError):
        pass

def listenelemente(path):
    try:
        with open(path) as fh:
            data = yaml.safe_load(fh)
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

def budget_nach_zeit(path):
    try:
        with open(path) as fh:
            data = yaml.safe_load(fh)

            del data['Budgetplaner'][0]

            return data['Budgetplaner']

    except (RuntimeError, TypeError, NameError):
        pass

def add_transaction(path, buchung):

    data = None

    try:
        with open(path) as fh:
            data = yaml.safe_load(fh)

            data['Budgetplaner'].append(buchung)

        with open(path, 'w') as outfile:  # Dictionary zurück in YAML schreiben
             yaml.dump(data, outfile, default_flow_style=False)
    except (RuntimeError, TypeError, NameError):
        pass

def remove_trans(path, details, summe, tag, monat, jahr):

    data = None

    try:
        with open(path) as fh:
            data = yaml.safe_load(fh)

            for e in data['Budgetplaner']:
                if 'archiviert' in e:
                    continue
                if e['Details'] == details and e['Summe'] == summe and e['Tag'] == int(tag) and e['Monat'] == monat and e['Jahr'] == int(jahr):

                    zudel = data['Budgetplaner'].index(e)

                    del data['Budgetplaner'][zudel]

                    break

        with open(path, 'w') as outfile:  # Dictionary zurück in YAML schreiben
             yaml.dump(data, outfile, default_flow_style=False)

    except:
        pass



