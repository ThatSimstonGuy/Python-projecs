
current_balance = 10000

while True:
    print('=====// DIDDY INTERNATIONAL BANKS \\=====')
    print('=====// ATM MENU \\=====')

    print('Current Balance:R', current_balance)

    print(' 1. Check Balance\n 2. Withdraw Money\n 3. Deposit Money\n 4. Exit')

    choice = int(input('Enter your choice:'))


    if choice == 1:
        print('Your current balance is:', current_balance)

    elif choice == 2:
        withdrawal_amount = int(input('Enter withdrawal amount:'))
        if withdrawal_amount > current_balance:
            print('Insufficient Funds')

        else:
            new_balance =  current_balance - withdrawal_amount
            print('Your current balance is:', new_balance)

    elif choice == 3:
        deposit_amount = int(input('Enter Deposit Amount:'))
        new_balance = deposit_amount + current_balance
        print('Your NEW balance is:', new_balance)

    elif choice == 4: 
        print('Thank you for using Diddy International')
        exit()

    else:
        print('Incorrect Values Enter Again')