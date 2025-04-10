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

deposit()