import re

user_sentence = input()

pattern = r"\b_([A-Za-z0-9]+)\b"

matches = re.findall(pattern, user_sentence)

print(",".join(matches))
