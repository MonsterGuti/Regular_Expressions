import re

dates = input()

regex = r"(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})"

matches = re.findall(regex, dates)

for date in matches:
    print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")
