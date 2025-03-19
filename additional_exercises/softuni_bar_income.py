import re

name_regex = r"(?<=%)[A-Z][a-z]+(?=%)"
product_regex = r"(?<=<)\w+(?=>)"
count_regex = r"(?<=\|)\d+(?=\|)"
price_regex = r"(?<=\|)(\d+(\.\d+)?)\$(?=\s)"

total_income = 0

while True:
    user_input = input()
    if user_input == "end of shift":
        break

    name_match = re.search(name_regex, user_input)
    product_match = re.search(product_regex, user_input)
    count_match = re.search(count_regex, user_input)
    price_match = re.search(price_regex, user_input)

    if name_match and product_match and count_match and price_match:
        name = name_match.group()
        product = product_match.group()
        count = int(count_match.group())
        price = float(price_match.group(1))

        total_price = count * price
        total_income += total_price
        print(f"{name}: {product} - {total_price:.2f}$")

print(f"Total income: {total_income:.2f}$")
