"""SKILLS: FUNCTIONS

Please complete the following promps.
"""

#################### PART 1 ####################

"""PROMPT 1

Write a function that returns `True` if a town name matches the name of your
hometown.

Examples: (let's say my hometown is San Francisco)
    - 'Oakland' -> False
    - 'San Francisco' -> True

Arguments:
    - The name of a town (str)

Return:
    - True or False (bool)
"""

# Write your function here

def hometown_match(my_hometown):
# Get user input    
    print(f"What's your hometown? Please type it: ")
    yr_hometown = input("> ")

# Check input against function argument.
    if yr_hometown == my_hometown:
        print(f"We are both from {my_hometown}!")    
    else:
        print(f"We are not from the same place, but we can still get along.")

#test
#hometown_match("Coloo")
#ok

"""PROMPT 2

Write a function that takes in a first and last name and returns a full name.

Examples:
    - 'Brighticorn', 'Hackbright' -> 'Brighticorn Hackbright'

Arguments:
    - First name (str)
    - Last name (str)

Return:
    - Full name (str)
"""

# Write your function here
def full_name(first_name, last_name):
# use quotes carefully to get correct format for string output
    return f"'{first_name} {last_name}'"

# test
# print(full_name("Brighty", "Hackibecky"))
# ok

"""PROMPT 3

Write a function that prints a greeting.

If the person is from your hometown, print
    Hi <full name>, we're from the same place!

Otherwise, print
    Hi <full name>, I'd like to visit <town name>!

HINT: You can reuse the functions that you wrote in PROMPT 1 and Prompt 2.

Examples: (still assume my hometown is San Francisco)
    - 'Fido', 'Bark', 'Oakland' -> Hi Fido Bark, I'd like to visit Oakland!
    - 'Mel', 'M', 'San Francisco' -> Hi Mel M, we're from the same place!

Arguments:
    - First name (str)
    - Last name (str)
    - Hometown (str)
"""

# Write your function here
def greeting(my_hometown):

# Get user input    
    print(f"What's your first name? Enter it here ")
    first_name = input("> ")

    print(f"What's your last name? Enter it here ")
    last_name = input("> ")

    print(f"What's your hometown? Type it here ")
    yr_hometown = input("> ")

# Check hometown input string against hometown string given in the argument.
    if yr_hometown == my_hometown:
        print(f"Hey {first_name}, we are both from {my_hometown}!")    
    else:
        print(f"Well, {first_name}, I'd love to visit {yr_hometown}.")

# test
# greeting("Shyann")
# ok


"""PROMPT 4

Write a function that returns True if a fruit is a berry.

Valid berries are:
    - strawberry
    - raspberry
    - blackberry
    - currant

Examples:
    - currant -> True
    - durian -> False

Arguments:
    - A fruit (str)

Return:
    - True or False (bool)
"""

# Write your function here

# define a list of valid fruits
berries = ['strawberry', 'raspberry', 'blackberry', 'currant']

def valid_fruit(fruit):
# if function argument is in a list of valid fruit
# return True
    valid_fruit = berries
    if fruit in valid_fruit:
        return True
    else:
        return False    

# test
# print(valid_fruit("strawberry"))
# print(valid_fruit("strawbeer"))        
# ok

"""PROMPT 5

Write a function that returns the shipping cost of an item.

Berries cost $0 to ship. Everything else costs $5.

Arguments:
    - Something that needs to be shipped (str)

Return:
    - Shipping cost (int)
"""

# Write your function here
def shipping_cost(item_to_ship):
# check if item to ship is berries
    if item_to_ship == "berries":
        print(f"There is no charge to ship berries.")
        return 0

    else:
        print(f"The cost of shipping {item_to_ship} is $5.00.")
        return 5 

# test
# print(shipping_cost("berries") + shipping_cost("beer"))
# print(f"TOTAL")
# ok

"""PROMPT 6

Write a function that returns the total cost of something by applying
taxes and fees of various states.

States will be given as their two-letter abbreviations. For example,
California's abbreviation is 'CA'.

There are some states with special fees. All fees should be added to the new
subtotal *after* tax:
    - CA (California): add a 3% (0.03) tax for recycling
    - PA (Pennsylvania): add $2.00 safety fee
    - MA (Massachusettes):
        - add $1.00 for items with a base price of $100.00 or less
        - add $3.00 for items over $100.00

Arguments:
    - Base price (int)
    - Two-letter state abbreviation (str)
    - Tax percentage as a decimal (optional, float)
        - If a tax percentage is not given, it defaults to 0.05 (or 5%)

Return:
    - Total price after taxes and fees (float)
"""

# Write your function here
# Cost of something with parameters for base price, location by state, and state tax  
# take defaults into account

ca_tax = float(0.03)
pa_fee = float(2.00)
ma_breakpoint_price = 100

def total_cost(base_price, location, decimal_tax=0.05, fees=0):

# check for location-based exceptions to the defaults
    if location == "CA":
        decimal_tax = ca_tax
    elif location == "PA":
        fees = pa_fee
    elif location == "MA": 
        if base_price <= ma_breakpoint_price:
            ma_fee = float(1.00) 
        else:
            ma_fee = float(3.00)
        fees = ma_fee
# output is base_price + (base_price * decimal_tax based on location) + fees based on location
    return base_price + (base_price * decimal_tax) + fees

#test
#print(total_cost(100,"MA"))
#print(total_cost(100,"PA"))
#print(total_cost(100,"CA"))
#print(total_cost(100,"IA"))
#ok

"""PROMPT 7

Write a function that takes in a list and *any* number of additional arguments.
The function should add all those items to the end of the  list and return
the list.

We haven't taught you how to do this! You'll need to do some research on your
own --- find a way to write a Python function that can take in an arbitrary
amount of arguments.

Arguments:
    - A list (list)
    - Additional args

Return:
    - A list with arguments added to the end (list)
"""

# Write your function here
# new thing is (*args)
# reference here: https://stackoverflow.com/questions/52430484/how-can-i-create-a-list-out-of-the-arguments-given-in-a-function

def lot_o_list(*things):
    convert_things = list(things)
    for thing in convert_things:
        return things

# test
# print(lot_o_list("mike", 3, 876, "jj"))
# ok

"""PROMPT 8

Write a function that takes in a word and returns a tuple. You'll do this in an
interesting way though, so make sure you read these directions thoroughly.

The tuple will contain two items:
    - The given word
    - The given word, multiplied 3 times

To do this, your function will create an *inner* function. The *inner*
function will multiply the given word by 3 and return it.

Then, the outer function will call the *inner* function to create a tuple.

Examples:
    - 'hi' -> ('hi', 'hihihi')

Arguments:
    - A word (str)

Return:
    - (word, wordx3) (tuple)
"""

# Write your function here
def tuple_x3(word):
# concatenate the argument passed
    triple_word = (word + word + word)
# form a tuple   
    tuple_words = (word, triple_word)   
    print(tuple_words)

# test
# tuple_x3("sun")
# ok   