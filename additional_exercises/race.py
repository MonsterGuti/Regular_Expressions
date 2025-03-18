import re

people_list = input().split(", ")
racers = {name: 0 for name in people_list}

name_pattern = r"[A-Za-z]+"
distance_pattern = r"\d"

while True:
    command = input()
    if command == "end of race":
        break

    name = "".join(re.findall(name_pattern, command))
    distance = sum(map(int, re.findall(distance_pattern, command)))

    if name in racers:
        racers[name] += int(distance)

filtered_racers = sorted(racers.items(), key=lambda x: -x[1])

print(f"1st place: {filtered_racers[0][0]}")
print(f"2nd place: {filtered_racers[1][0]}")
print(f"3rd place: {filtered_racers[2][0]}")
