import random

# cap letter means constants
MAX_BET = 10000
MIN_BET = 10
MAX_LINES = 3

ROWS = 3
COLS = 3


# dictionary - similar to hashmap
symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 8,
    "B" : 6,
    "C" : 4,
    "D" : 2
}

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

def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        # _ means a throwaway variable name. It's used when the loop variable isn't going to be used
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range (cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range (rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_spin(columns):
    # first we need to transpose the matrix, because the values are stored in the form of cols and not rows

    for row in range (len(columns[0])):
        # enumerate gives number to i, basically indices
        for i, column in enumerate(columns):
            if(i != len(columns) - 1):
                print(column[row], "|", end=" ")
            else:
                print(column[row])

    print([len(col) for col in columns])


def check_win(cols, lines, bet, values):
    print()

def main():
    balance = deposit()
    lines = get_num_of_lines()
    check_bet(balance, lines)
    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot_spin(slots)

    # print(f"Amount deposited: ${balance}, \nNo. of lines: ${lines}, \nAmount betted: ${bet}")

main()