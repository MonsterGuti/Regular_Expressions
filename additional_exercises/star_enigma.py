import re

n = int(input())

attacked_planets = []
destroyed_planets = []

for i in range(n):
    encrypted_message = input()

    star_count = sum(1 for char in encrypted_message.lower() if char in "star")

    decrypted_message = ''.join(chr(ord(char) - star_count) for char in encrypted_message)

    match = re.search(r"@([A-Za-z]+).*:(\d+).*!(A|D)!.*->(\d+)", decrypted_message)

    if match:
        planet_name = match.group(1)
        attack_type = match.group(3)

        if attack_type == 'A':
            attacked_planets.append(planet_name)
        elif attack_type == 'D':
            destroyed_planets.append(planet_name)

attacked_planets.sort()
destroyed_planets.sort()

print(f"Attacked planets: {len(attacked_planets)}")
for planet in attacked_planets:
    print(f"-> {planet}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in destroyed_planets:
    print(f"-> {planet}")
