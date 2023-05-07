import math  # Imports math functions into this file

# The section below will print the entire paragraph for the user to see and read
print("Choose either 'investment' or 'bond from the menu below to proceed:\n ")
print("Investment  -  To calculate the amount of interest you'll earn on your investment.")
print("Bond        -  To calculate the amount you have to pay on a home loan.\n ")

# Requests user input of either 'investment' or 'bond' and turns into lower case for program to continue
# Accepts any capitlisation of both words
user_input = str(input("Please choose 1 of the above: ")).lower()
print(" ")

# If 'investment choice is chosen, the program will carry out this 'if' statement
# Asks the user to input the following information as mainly integers
# ...as calculations will need to be done further down
# Another choice of 'simple' or 'compound' is given to the user to work out different interest amounts
if user_input == 'investment':
    user_deposit = float(input("How much are you going to deposit (£): "))
    user_interest_rate = float(input("The current interest rate on your deposit (in %): "))
    user_invest_years = int(input("How many years are you planning to invest your money for?: "))
    user_interest_type = str(input("Would you like to go with 'simple' or 'compound' interest?: ")).lower()

# If 'simple' interest is chosen, this 'if' statement will be initiated
# A forumla for simple interest will take all of the information from the user and calculate their interest
# The 'round(" ", 2)' section will round the value in " " to 2 decimal places.
# An output will be given to the user to show what they have input and a total final interest gained!
    if user_interest_type == 'simple':
        total_simple = user_deposit * (1 + (user_interest_rate / 100) * user_invest_years)
        print(" ")
        print('Based on the following information; ')
        print(" ")
        print(f'A deposit of:                                      £{user_deposit}')
        print(f'An interest rate of:                                {user_interest_rate}%')
        print(f'The amount of years you plan to invest for:         {user_invest_years} years')
        print(f'An interest type of:                                {user_interest_type}')
        print(" ")
        print(f'The interest accumulated on your deposit will be:    £{total_simple - user_deposit}')
        print(" ")
        print(f'Your total including deposit and interest will be:   £{round(total_simple, 2)}')

# If 'compound' interest is chosen, this 'if' statement will be initiated
# A formula for compound interest will take all of the information from the user and calculate their interest
# The 'round(" ", 2)' section will round the value in " " to 2 decimal places.
# An output will be given to the user to show what they have input and a total final interest gained!
    elif user_interest_type == 'compound':
        total_compound = user_deposit * math.pow((1 + (user_interest_rate/100)), user_invest_years)
        print(" ")
        print('Based on the following information; ')
        print(" ")
        print(f'A deposit of:                                      £{user_deposit}')
        print(f'An interest rate of:                                {user_interest_rate}%')
        print(f'The amount of years you plan to invest for:         {user_invest_years} years')
        print(f'An interest type of:                                {user_interest_type}')
        print(" ")
        print(f'The interest accumulated on your deposit will be:  £{round(total_compound - user_deposit, 2)}')
        print(" ")
        print(f'Your total including deposit and interest will be: £{round(total_compound, 2)}')

# If the option of 'bond' was chosen at the very start of the program, this 'if' statement will initiate
# The user will be asked to enter slightly different details from the 'investment' option.
# A different formula is also used here to calculate 'bond' interest.
# The 'round(" ", 2)' section will round the value in " " to 2 decimal places.
# An output will be given to the user to show what they have input and a total monthly bond repayment
elif user_input == "bond":
    user_house_value = int(input("What is your home currently valued at?: "))
    user_interest_rate = float(input("What is the current interest rate?: "))
    bond_months = int(input("The amount of months you intend to take to repay the bond?: "))
    monthly_interest = (user_interest_rate / 100) / 12
    total_bond = (monthly_interest * user_house_value) / (1 - (math.pow(1 + monthly_interest, - bond_months)))
    print(" ")
    print('Based on the following information; ')
    print(" ")
    print(f'A house value of:                                      £{user_house_value}')
    print(f'An interest rate of:                                    {user_interest_rate}%')
    print(f'Amount of repayment months:                             {bond_months}')
    print(f'The monthly interest:                                   {round(monthly_interest, 3)}%')
    print(" ")
    print(f'Your total monthly repayments will be:                 £{round(total_bond, 2)}')
elif user_input == " ":
    print("Please do not leave this option blank!")
elif user_input != "bond":
    print("Please enter the correct option!")

exit("Check complete, thanks for using finance calculator 1.0")
