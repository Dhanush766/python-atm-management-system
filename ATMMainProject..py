#ATMMainProject.py
from ATMExcept import DepositError, InSuffFundError, WithDrawError
from ATMMenu import menu
from ATMOperations import deposit, withdraw, balanceenq
while(True):
    try:
        menu()
        ch=int(input("Enter UR Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("\tDont'enter -VE OR ZERO Value for Deposit-try again" )
                except ValueError:
                    print("\tDon't Enter Alnums,strs and Symbols for Deposit--try again")
            case 2:
                try:
                    withdraw()
                except WithDrawError:
                    print("\tDont'enter -VE OR ZERO Value for Withdraw-try again")
                except InSuffFundError:
                    print("\tUr Account Does not Contain Suff Funds-Read Python Notes")
                except ValueError:
                    print("\tDon't Enter Alnums,strs and Symbols for Withdraw-try again")
            case 3:
                balanceenq()
            case 4:
                print("Thx for Using Project")
                break
            case _:
                print("\tUr Selection of Operation is Wrong-Try again")
    except ValueError:
        print("\tDon't Enter Alnums,strs and Symbols for Choice--try again")