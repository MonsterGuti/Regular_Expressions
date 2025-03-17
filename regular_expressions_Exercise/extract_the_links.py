import re

web_sites = input()

pattern = r"(www\.[A-Za-z0-9\-]+(\.[a-z]+)+)"

while web_sites:
    match = re.search(pattern, web_sites)
    if match:
        url = match.group(1)
        print(url)
    web_sites = input()