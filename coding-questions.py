#This has the code for the "Prework - Coding Question"
# You can also run this as a program if you desire
print("Welcome to the Prework - Coding Question")
print()



#       Question 1: def hello_name(user_name):
print("#Question 1:")
print("def hello_name(user_name):")
print("This prints out the username that is entered")
print("INPUT:")
print('hello_name("hello_USERNAME!")')

# Actual Code -----------------------------
def hello_name(user_name):
    print(user_name)

print()
print("OUTPUT:")
hello_name("hello_USERNAME!") # This shows you the result of the function
print()



#       Question 2: def first_odds():
print("Question 2:")
print("def first_odds():")
print("This creates a list of odd numbers between 1 and 100")
print("INPUT:")
print('first_odds()')

# Actual Code -----------------------------
def first_odds():
    for number in (range(1, 100, 2)):
        print(number)

print()
print("OUTPUT:")
first_odds() # This shows you the result of the function
print()



#       Question 3: def max_num_in_list(a_list):
print("Question 3:")
print("def max_num_in_list(a_list):")
print("This shows you the greatest number in a list")
print("INPUT:")
print('list = [1, 64, 41, 16, 7, 23, 18, 19, 29]')
print('print(max_num_in_list(list))')

# Actual Code -----------------------------
def max_num_in_list(a_list):
    return max(a_list)

print()
print("OUTPUT:")
list = [1, 64, 41, 16, 7, 23, 18, 19, 29] # This sets up the list to be used for the function
print(max_num_in_list(list)) # This shows you the result of the function
print()



#       Question 4: def is_leap_year(a_year):
print("Question 4:")
print("def is_leap_year(a_year):")
print("This shows you the year you entered if it is a leap year, returns True or False (Boolean)")
print("INPUT:")
print('print(is_leap_year(2024))')

# Actual Code -----------------------------
def is_leap_year(a_year):
    if (a_year % 4):
        return False
    elif(a_year % 400):
        if (a_year % 100): return True
        else: return False
    else: return True

print()
print("OUTPUT:")
print("Is leap year:")
print(is_leap_year(2024)) # This shows you the result of the function
print()



#       Question 5: def is_consecutive(a_list):
print("Question 5:")
print("def is_consecutive(a_list):")
print("This function sees if the list are consecutive, meaning that they go in order like 1, 2, 3, and 4. Also returns boolean")
print("INPUT:")
print('list_ii = [1, 2, 3, 4, 7, 8]')
print('print(is_consecutive(list))')

# Actual Code -----------------------------
def is_consecutive(a_list):
    place = -1
    setbool = 0
    listbool = [True]
    for number in a_list:
        previous_n = a_list[place]
        if (place > -1):
            listbool.append(False)
        if (number == previous_n+1):
            listbool[setbool] = True
        place += 1
        setbool += 1
    
    for case in listbool:
        if (case == False):
            return False
    return True

print()
print("OUTPUT:")
print("Is consecutive:")
list_ii = [1, 2, 3, 4, 7, 8] # This sets up the list to be used for the function
print(is_consecutive(list_ii)) # This shows you the result of the function
print()

# Final message
print("I really hope you enjoyed my sample functions, you have a great day!")