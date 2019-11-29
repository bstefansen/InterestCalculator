
print("")
amount = input("Enter amount: ")

def kReplace(amount):
    if "K" in amount:
        replace = amount.replace('K', '')
        replace = float(replace)*1000
        return replace
kReplace(amount)

print("")
print("Original: ", amount)
print("Changes: ", kReplace(amount))
print("")
