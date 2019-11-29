from decimal import *
getcontext().prec = 8

print("")
num = '${:,.2f}'.format(float(input("Enter a number: ")))
print("")

print(num)
print("")
