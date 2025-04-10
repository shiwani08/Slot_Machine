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
                print("The deposited amount is:",amount)
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
                print("The lines that you have entered is: ", lines)
                break
            else:
                print("Please enter between (1-" + str(MAX_LINES) + ")! ")

        except ValueError:
            print("Please enter a valid number!")

    return lines

def main():
    amount = deposit()
    lines = get_num_of_lines

main()