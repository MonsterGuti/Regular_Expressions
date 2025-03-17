import re

bought_furniture = []
total_cost = 0
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
furniture = input()

while furniture != "Purchase":
    match = re.search(pattern, furniture)
    if match:
        furniture_name, price, quantity = match.groups()
        bought_furniture.append(furniture_name)
        total_cost += int(quantity) * float(price)
    furniture = input()

print("Bought furniture: ")
for item in bought_furniture:
    print(item)

print(f"Total money spend: {total_cost:.2f}")
