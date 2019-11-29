
print("")
amount = input("Enter rate: ")

def percentReplace(amount):
    if "%" in amount:
        replace = amount.replace('%', '')
        return replace
percentReplace(amount)

print("")
print("Original: ", amount)
print("Changes: ", percentReplace(amount))
print("")
