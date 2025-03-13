import re

numbers = input()

regex = r"(^|(?<=\s))-?([0]|[1-9]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

number_matches = re.finditer(regex, numbers)

for match in number_matches:
    print(match.group(), end=" ")
