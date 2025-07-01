print('////** SOL.AR Bank **\\\\')

def update_account():

    account_number = input("Enter account number")
    account_type = input("Enter account type ('s' for savings, 'c' for checking): ")
    try:
        min_bal = float(1000)
        current_bal = float(input("Enter the current balance: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for balance.")
        return
    
    print("\n ***--- Account Summary ---***")
    print(f"Account Number: {account_number} \n")

    if account_type == 's':
        print("////--ACCOUNT TYPE: Savings--\\\\")
        if current_bal < min_bal:
            srvc_charge = 10.00
            current_bal -= srvc_charge
            print(f"Service charge of ${srvc_charge:.2f} applied.")
        else:
            intrest_rate = 0.04
            intrest_earned = current_bal * intrest_rate
            current_bal += intrest_earned
            print(f"Intrest earned: ${intrest_earned:.2f} (4%)")
    elif account_type == 'c':
        print("----- ACCOUNT TYPE: Checking -----")
        if current_bal < min_bal:
            srvc_charge = 25.00
            current_bal -= srvc_charge
            print(f"Service charge of ${srvc_charge:.2f} applied.")
        else:
            bal_above_min = current_bal - min_bal
            if bal_above_min <= 5000:
                intrest_rate = 0.03
                intrest_earned = current_bal * intrest_rate
                current_bal += intrest_earned
                print(f"Interest earned: ${intrest_earned:.2f} (3%)")
            else:
                intrest_rate = 0.05
                intrest_earned = current_bal * intrest_rate
                current_bal += intrest_earned
                print(f"Interest earned: ${intrest_earned:.2f} (5%)")
    else:
        print("Invalid account type.")
        return
            
    print(f"Current Balance: ${current_bal:.2f}")
    print("***--- End of Summary ---***")

if __name__ == "__main__":
    update_account()


