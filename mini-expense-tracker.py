import json

try:
    data = json.load(open("data.json", "r"))
except:
    data = []

while True:
    amount = input("Сумма (или stop): ")
    if amount == "stop":
        break

    data.append(int(amount))

with open("data.json", "w") as f:
    json.dump(data, f)

print("Итог:", sum(data))
