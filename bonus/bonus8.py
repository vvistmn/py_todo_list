date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("Let your thoughts flow: ").capitalize()

with open(f"../journal/{date}.txt") as file:
    content = file.readlines()

with open(f"../journal/{date}.txt", 'w') as file:
    content.append(f"date: {date}.\n")
    content.append(f"Mood user today: {mood}.\n")
    content.append(f"Thoughts user: {thoughts}\n")
    content.append("\n")

    file.writelines(content)