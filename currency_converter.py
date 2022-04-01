with open('currency_data.txt') as f:
    lines = f.readlines()

# print(lines)
currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter amount in INR:\n"))
print("Enter the name of currency you want to convert this amount to\nAvailable options:\n")
[print(i) for i in currencyDict.keys()]
currency = input("Please enter one of these values: \n")
print(f"{amount} INR is equal to {amount * float(currencyDict[currency]) } {currency}")

print('NOTE : this data is collected on "Mar 11, 2022 08:08 UTC"')