print("")
amount = input("Enter amount: ")

def dlrReplace(amount):
    if amount[0] == "$":
        replace = amount.replace('$', 'A')
        return replace

def findDlr(amount):
    print(amount[0])

dlrReplace(amount)

print("")
print("Original: ", amount)
print("Changes: ", dlrReplace(amount))
print("")
