import re

input_line = input().strip()

demons = [d.strip() for d in input_line.split(",")]

demon_details = []

for demon in demons:
    health = 0
    damage = 0
    multiplier = 1

    for char in demon:
        if char.isalpha():
            health += ord(char)

    numbers = re.findall(r'[+-]?\d+\.\d+|[+-]?\d+', demon)

    for num in numbers:
        if num == "*" or num == "/":
            if num == "*":
                multiplier *= 2
            elif num == "/":
                multiplier /= 2
        else:
            damage += float(num)

    damage *= multiplier
    demon_details.append((demon, health, damage))

demon_details.sort(key=lambda x: x[0])

for demon, health, damage in demon_details:
    print(f"{demon} - {health} health, {damage:.2f} damage")
