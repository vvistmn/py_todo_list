def get_average():
    with open('../files/data.txt', 'r') as file:
        data = file.readlines()

    data = data[1:] # Игнорируем первый элемент
    data = [float(i) for i in data]
    def_average = sum(data) / len(data)
    return def_average


average = get_average()
print(average)