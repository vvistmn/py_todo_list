def parse(values):
    data = {}
    parts = values.split(' ')

    data['feet'] = float(parts[0])
    data['inches'] = float(parts[1])
    
    return data


def convert(feet, inches):
    return feet * 0.3048 + inches * 0.0254


feet_inches = input('Enter feet amd inches: ')
data_parse = parse(feet_inches)
meters = convert(inches=data_parse['inches'], feet=data_parse['feet'])

print(f"{data_parse['feet']} feet and {data_parse['inches']} inches is equal to {meters} meters.")

if meters < 1:
    print('Kid is too small')
else:
    print('Kid can ise the slide')