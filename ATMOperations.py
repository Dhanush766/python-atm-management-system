from ATMExcept import DepositError, WithDrawError, InSuffFundError

bal = 500.00


def deposit():
    global bal

    damt = float(input("Enter Your Deposit Amount: "))

    if damt <= 0:
        raise DepositError

    bal = bal + damt

    print("\tAccount xxxxxxx123 credited with INR:", damt)
    print("\tBalance after deposit INR:", bal)


def withdraw():
    global bal
    wamt = float(input("Enter Your Withdraw Amount: "))
    if wamt <= 0:
        raise WithDrawError
    if wamt > bal:
        raise InSuffFundError
    bal = bal - wamt
    print("\tAccount xxxxxxx123 debited with INR:", wamt)
    print("\tBalance after withdrawal INR:", bal)

def balanceenq():
    print("\tAccount xxxxxxx123 Balance INR:", bal)