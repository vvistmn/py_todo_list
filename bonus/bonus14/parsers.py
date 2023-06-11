def parse(values):
    data = {}
    parts = values.split(' ')

    data['feet'] = float(parts[0])
    data['inches'] = float(parts[1])

    return data
