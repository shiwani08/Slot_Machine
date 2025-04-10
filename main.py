# cap letter means constants
MAX_BET = 10000
MIN_BET = 10
MAX_LINES = 3

def deposit():
    # checking if the entered amount is a positive number
    while True: 
        amount = input("How much amount would you like to deposit? ")

        # checking if the entered string value is a digit
        try:
            amount = int(amount)
            if(amount > 0):
                break
            else:
                print("Enter a positive amount!")

        except ValueError:
            print("Please enter a number!")
    
    return amount

def get_num_of_lines(): 
    while True: 
        lines = (input("Enter the number of lines to bet on between (1-" + str(MAX_LINES) + ")! "))

        try:
            lines = int(lines)
            if(1 <= lines <= MAX_LINES):
                break
            else:
                print("Please enter between (1-" + str(MAX_LINES) + ")! ")

        except ValueError:
            print("Please enter a valid number!")

    return lines

def get_bet():
    while True: 
        amount = input("How much amount would you like to bet? ")

        # checking if the entered string value is a digit
        try:
            amount = int(amount)
            if(MIN_BET <= amount <= MAX_BET):
                break
            else:
                print(f"Amount should be between ${MIN_BET} - ${MAX_BET}")

        except ValueError:
            print("Please enter a number!")
    
    return amount

def check_bet(balance, lines):
    while True: 
        bet = get_bet()
        total_bet = bet * lines

        if(total_bet <= balance):
            balance = balance - total_bet
            print(f"You are betting ${bet} on {lines}. \nYour total bet is: ${total_bet}. \nAmount left: ${balance}")

        else:
            print(f"You do not have sufficient balance! Amount left: ${balance}")
            break

def main():
    balance = deposit()
    lines = get_num_of_lines()
    check_bet(balance, lines)

    # print(f"Amount deposited: ${balance}, \nNo. of lines: ${lines}, \nAmount betted: ${bet}")

main()