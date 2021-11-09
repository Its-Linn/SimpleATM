from datetime import date
import random
pin = 1234
name = 'Steve'
today = date.today()
balance = 50000
chance = 3
registered_atm = {}
key = 833120
resi = random.randint(10000,100000)

def homescreen():
    print('Welcome To Test Bank')
    print('''
    ---------------------------------------------------
    - (1) Check Balance      (4) Deposit
    - (2) Sent Money         (5) Regist ATM Rekening
    - (3) Withdraw           (6) Quit
    ---------------------------------------------------''')
    menu()
def amountInfo():
    print(f'''
    -------------------------
    - Name: {name}
    - Balance: {balance}
    - Date: {today}
    -------------------------
    ''')
    box = ['y','n']
    while True:
        back = input('Go Back To Menu [Y/N]: ').lower()
        if back.isalpha():
            if back not in box:
                print('Y or N')
                continue
            if back in box and back == 'y':
                homescreen()
            elif back == 'n' and back in box:
                quit()
        else:
            print('Y or N!!!')
def withdraw():
    global balance
    print('''
    ------------------------------
    - (1) 10.000    (4) 100.000
    - (2) 25.000    (5) More
    - (3) 50.000
    ------------------------------
    ''')
    withdraw_amount = int(input('Number: '))
    def wdraw(a,b):
        print(f'''
        -------------------------
        - No: {resi}
        - Name: {name}
        - Withdraw: {a}
        - Balance: {b}
        - Date: {today}
        -------------------------
        ''')
        backs = ['y', 'n']
        while True:
            back = input('Go Back To Menu [Y/N]: ').lower()
            if back.isalpha() == True:
                if back == 'y' and back in backs:
                    homescreen()
                if back == 'n':
                    quit()
                if back not in backs:
                    print('Y or N')
                    continue
            else:
                print('Y or N!!!')
    if withdraw_amount == 1:
        amount = 10000
        if amount > balance:
            print('Insufficent Balance, Your Balance is: ')
            amountInfo()
        balance = balance - amount
        wdraw(amount,balance)
    elif withdraw_amount == 2:
        amount = 25000
        if amount > balance:
            print('Insufficent Balance, Your Balance is: ')
            amountInfo()
        balance = balance - amount
        wdraw(amount,balance)
    elif withdraw_amount == 3:
        amount = 50000
        if amount > balance:
            print('Insufficent Balance, Your Balance is: ')
            amountInfo()
        balance = balance - amount
        wdraw(amount,balance)
    elif withdraw_amount == 4:
        amount = 100000
        if amount > balance:
            print('Insufficent Balance, Your Balance is: ')
            amountInfo()
        balance = balance - amount
        wdraw(amount,balance)
    elif withdraw_amount == 5:
        amount = int(input('Enter Amount: '))
        if amount > balance:
            print('Insufficent Balance, Your Balance is: ')
            amountInfo()
        balance = balance - amount
        wdraw(amount,balance)
    else:
        print('Enter The Right Number!!!')
        withdraw()
def sentmoney():
    global balance
    def recepient(a,b):
        to = str(input('Recepient Name/Phone Number: '))
        if to in registered_atm:
            too = registered_atm[to]
        else:
            print('Nama Tidak Terdaftar')
        print(f'''
        -------------------------
        - No: {resi}
        - Name: {name}
        - Recepient: {too} - {to}
        - Amount: {a}
        - Balance: {b}
        - Status: Success
        - Date: {today}
        -------------------------
        ''')
        box = ['y','n']
        while True:
            back = input('Go Back To Menu [Y/N]: ').lower()
            if back.isalpha() == True:
                if back not in box:
                    print('Y or N')
                    continue
                elif back == 'y' and back in box:
                    homescreen()
                elif back == 'n':
                    quit()
            else:
                print('Y or N')
    print('''
    -------------------------
    - (1) 10.000    (4) 100.000
    - (2) 25.000    (5) More
    - (3) 50.000
    -------------------------
    ''')
    num = int(input('Enter Number: '))
    if num == 1:
        amount = 10000
        if amount > balance:
            print('Insufficent Balance, Your Balance is: ')
            amountInfo()
        balance -= amount
        recepient(amount,balance)
    elif num == 2:
        amount = 25000
        if amount > balance:
            print('Insufficent Balance, Your Balance is: ')
            amountInfo()
        balance -= amount
        recepient(amount,balance)
    elif num == 3:
        amount = 50000
        if amount > balance:
            print('Insufficent Balance, Your Balance is: ')
            amountInfo()
        balance -= 50000
        recepient(amount,balance)
    elif num == 4:
        amount = 100000
        if amount > balance:
            print('Insufficent Balance, Your Balance is: ')
            amountInfo()
        balance -= amount
        recepient(amount,balance)
    elif num == 5:
        amount = int(input('Enter Amount: '))
        if amount > balance:
            print('Insufficent Balance, Your Balance is: ')
            amountInfo()
        balance -= amount
        recepient(amount,balance)
    else:
        print('Enter The Right Number!!!')
        sentmoney()
def deposit():
    global balance
    def profile(a,b):
        print(f'''
        -------------------------
        - No: {resi}
        - Name: {name}
        - Deposit: {a}
        - Balance: {b}
        - Date: {today}
        -------------------------
        ''')
        box = ['y','n']
        while True:
            back = input('Go Back To Menu [Y/N]: ').lower()
            if back.isalpha() == True:
                if back not in box:
                    print('Y or N')
                    continue
                elif back == 'y' and back in box:
                    homescreen()
                elif back == 'n' and back in box:
                    quit()
            else:
                print('Y or N')
    print('''
    ------------------------------
    - (1) 10.000    (4) 100.000
    - (2) 25.000    (5) More..
    - (3) 50.000
    ------------------------------
    ''')
    box = [1,2,3,4,5]
    while True:
        choice = input('Enter Option: ')
        if choice.isalpha() == True:
            if int(choice) == 1 and int(choice) in box:
                amount = 10000
                balance += amount
                profile(amount,balance)
            elif int(choice) == 2 and int(choice) in box:
                amount = 25000
                balance += 25000
                profile(amount,balance)
            elif int(choice) == 3 and int(choice) in box:
                amount = 50000
                balance += 50000
                profile(amount,balance)
            elif int(choice) == 4 and int(choice) in box:
                amount = 100000
                balance += 100000
                profile(amount,balance)
            elif int(choice) == 5 and int(choice) in box:
                amount = int(input('Enter Amount: '))
                balance += amount
                profile(amount,balance)
        else:
            continue
def regis():
    nama = str(input('Atas Nama: '))
    rekening = int(input('No Rekening: '))
    registered_atm[nama] = rekening
    homescreen()
def menu():
    box = [1,2,3,4,5,6]
    while True:
        pilih = input('Enter The Action Number: ')
        if pilih.isnumeric() == True:
            if int(pilih) not in box:
                continue
            elif int(pilih) in box and int(pilih) == 1:
                amountInfo()
            elif int(pilih) == 2 and int(pilih) in box:
                sentmoney()
            elif int(pilih) == 3 and int(pilih) in box:
                withdraw()
            elif int(pilih) == 4 and int(pilih) in box:
                deposit()
            elif int(pilih) == 5 and int(pilih) in box:
                regis()
            elif int(pilih) == 6 and int(pilih) in box:
                quit()
            else:
                print('Choose 1 to 6!!!')
        else:
            print('Enter Number Only!!')
#------------------------------------------ATM LOGIC Section--------------------------------------------------------
def login():
    npin = input('Enter Pin Again: ')
    if int(npin) == pin or int(user_pin) == pin:
        print('Welcome To Test Bank')
        print('''
        ----------------------------------------
        - (1) Check Balance      (4) Deposit
        - (2) Sent Money         (5) Regist ATM Rekening
        - (3) Withdraw           (6) Quit
        ----------------------------------------
        ''')
        menu()
    else:
        print('Wrong Pin')
while chance != 0:
    user_pin = input('Enter Pin: ')
    if int(user_pin) == pin:
        login()
    if chance == 1:
        forgot = input('Forgot Pin?. [Reset/No]: ').lower()
        box = ['reset','no','r','n']
        if forgot not in box:
            print('Reset Or No')
            continue
        if forgot in box:
            restpwd = input('Enter Security Key: ')
            if restpwd.isnumeric() == True and int(restpwd) == key:
                nkey = input('Enter New Pin: ')
                if nkey.isnumeric() == True:
                    pin = int(nkey)
                    login()
                else:
                    print('Only Enter Number!!')
                    continue
            else:
                print('Wrong Security Key!!!')
                quit()
        elif forgot == 'no':
            break
    if user_pin.isnumeric() == True:
        if int(user_pin) != pin:
            chance -= 1
            print('Wrong Pin')
            print(f'You have {chance} Chances Left.')
        else:
            break
    else:
        print('PIN ONLY CONTAIN NUMBER!!!')