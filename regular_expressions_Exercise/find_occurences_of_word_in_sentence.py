import re

user_sentence = input()
searched_word = input()

pattern = fr"(?i)\b{searched_word}\b"

matches = re.findall(pattern, user_sentence)

print(len(matches))