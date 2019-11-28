# Filename: BES_Interests.property
# Description: A program that calculates the interest on a loan
# Author: Blake Stefansen


def intro():
    print("")
    print("Welcome to the interest calculator")
    print("")

def calc(loanAmount, rate):
    return

def output(loanAmount, rate):
    rateDecimal = rate*0.01
    interest = loanAmount*rateDecimal
    print("")
    print("Loan amount: $" + str(loanAmount))
    print("Interest rate: " + str(rate) + "%")
    print("Interest amount: $" + str(interest))
    print("")

def again():
    againAnswer = input("Continue? (y/n): ")
    if againAnswer == "y":
        main()
    else:
        print("")

def outro():
    print("Bye!")
    print("")

def main():
    intro()
    loanAmount = float(input("Enter loan amount: $"))
    rate = float(input("Enter interest rate: %"))
    calc(loanAmount, rate)
    output(loanAmount, rate)
    again()
    outro()

if __name__ == '__main__':
    main()
