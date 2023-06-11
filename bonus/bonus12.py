feet_inches = input('Enter feet amd inches: ')


def convert(values):
    parts = values.split(' ')
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet * 0.3048 + inches * 0.0254
    return {'meters': meters, 'message': f"{feet} feet and {inches} inches is equal to {meters} meters."}


result = convert(feet_inches)
print(result['message'])

if result['meters'] < 1:
    print('Kid is too small')
else:
    print('Kid can ise the slide')