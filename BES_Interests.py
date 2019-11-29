# Filename: BES_Interests.property
# Description: A program that calculates the interest on a loan
# Author: Blake Stefansen


#//TODO: use the decimal class
#        add comments

def intro():
    print("")
    print("Welcome to the interest calculator")
    print("")

def dlrTest(loanAmount):
    if loanAmount[0] == "$":
        newLoanAmount = loanAmount.replace("$", "")
        return newLoanAmount
    return loanAmount

def commaTest(loanAmount):
    if "," in loanAmount:
        newLoanAmount = loanAmount.replace(",", "")
        return newLoanAmount
    return loanAmount

def kTest(loanAmount):
    if "K" in loanAmount:
        newLoanAmount = loanAmount.replace("K", "")
        newLoanAmount = float(newLoanAmount)*1000
        return newLoanAmount
    return loanAmount

def percentTest(rate):
    if "%" in rate:
        replace = rate.replace("%", "")
        return replace
    return rate

def calc(loanAmount, rate):
    rateDecimal = float(rate)*0.01
    interest = float(loanAmount)*rateDecimal
    return interest

def output(loanAmount, rate):
    print("")
    print("Loan amount: " + str('${:,.2f}'.format(float(loanAmount))))
    print("Interest rate: " + str('{:.3f}%'.format(float(rate))))
    print("Interest amount: " + str('${:,.2f}'.format(float(calc(loanAmount, rate)))))
    print("")

def again():
    againAnswer = input("Continue? (y/n): ")
    if againAnswer == "y":
        main()
    else:
        print("")
        print("Bye!")
        print("")

def main():
    intro()
    loanAmount = str(input("Enter loan amount: "))
    rate = str(input("Enter interest rate: "))
    dlrTest(loanAmount)
    loanAmount = dlrTest(loanAmount)
    commaTest(loanAmount)
    loanAmount = commaTest(loanAmount)
    kTest(loanAmount)
    loanAmount = kTest(loanAmount)
    percentTest(rate)
    rate = percentTest(rate)
    calc(loanAmount, rate)
    output(loanAmount, rate)
    again()

if __name__ == '__main__':
    main()
