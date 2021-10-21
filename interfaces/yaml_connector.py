import yaml


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

            print(data['Budgetplaner'])

            data['Budgetplaner'].append(buchung)

            print(data['Budgetplaner'])

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

                    print("1->",data['Budgetplaner'])

                    zudel = data['Budgetplaner'].index(e)

                    print("2->", data['Budgetplaner'][data['Budgetplaner'].index(e)])

                    del data['Budgetplaner'][zudel]

                    print("3->", data['Budgetplaner'])

                    break

        with open(path, 'w') as outfile:  # Dictionary zurück in YAML schreiben
             yaml.dump(data, outfile, default_flow_style=False)

    except:
        pass



