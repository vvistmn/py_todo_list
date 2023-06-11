import pathlib

path_to_dir = f"{pathlib.Path().resolve()}/../files/"

contents = [
    'Text 1.',
    'Text 2.',
    'Text 3.'
]

filenames = [
    'doc.txt',
    'report.txt',
    'presentation.txt'
]

for content, filename in zip(contents, filenames):
    file = open(f"{path_to_dir}{filename}", 'w')
    file.write(content)
    file.close()

print('Bye')

a = 'I am a string' \
    ' on my own'
