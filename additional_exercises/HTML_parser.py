import re

html_content = input()

title_match = re.search(r'<title>(.*?)</title>', html_content)
title = title_match.group(1) if title_match else ""

body_match = re.search(r'<body>(.*?)</body>', html_content)
body_content = body_match.group(1) if body_match else ""

body_content = re.sub(r'<.*?>', '', body_content)

print(f"Title: {title}")
print(f"Content: {body_content.strip()}")
