#EXERCISE 1 String Formatting
'''
Python uses C-style string formatting to create new, formatted strings.
The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list),
together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".

Let's say you have a variable called "name" with your user name in it, and you would then like to print(out a greeting to that user.)
'''
'''
# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)



# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))


# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)




data = ("John", "Doe", 12.000)
print("Hello %s  %s. your current balance is %.3f" % data)

'''

'''
Here are some basic argument specifiers you should know:

%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase
'''

#EXERCISE 2 Basic String Operations
'''
astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

astring = "Hello world!"
print(astring.index("o")) #That prints out 4, the first occurrence of the letter "o"

astring = "Hello world!"
print(astring.count("l")) #counts the number of l's

astring = "Hello world!" # starting at index 3, and ending at index 6( yes 6) 
print(astring[3:7])


astring = "Hello world!"    #3 to 7 skipping one character.[start:stop:step].
print(astring[3:7:2])

astring = "Hello world!" #can easily reverse a string like this
print(astring[::-1])

astring = "Hello world!" #ll letters converted to uppercase and lowercase,
print(astring.upper())
print(astring.lower())

astring = "Hello world!"
print(astring.startswith("Hello")) #starts with something or ends with something,
print(astring.endswith("asdfasdfasdf"))

astring = "Hello world!"    #splits at a space,
afewwords = astring.split(" ")
print (afewwords)
print('There are ',len(afewwords),'afewwords')
'''
#Conditions
'''
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True
'''

#Boolean operators 'and' 'or'
'''
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
'''

# The "in" operator
'''
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

'''
#Python uses indentation to define code blocks, instead of brackets.
#The standard Python indentation is 4 spaces, although tabs and any other space size will work,
#as long as it is consistent. Notice that code blocks do not need any termination.
'''
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")
'''

# The 'is' operator
#It tests if two variables point the same object, not if two variables have the same value.
'''
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False
'''

#The 'not' operator
'''
print(not False) # Prints out True
print((not False) == (False)) # Prints out False

'''

# The "for" loop
'''
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)


'''
'''
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

'''

#The 'while' operator
# Prints out 0,1,2,3,4
'''
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

'''


# "break" and "continue" statements
# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break #break is used to exit a for loop or a while loop

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue #whereas continue is used to skip the current block, and return to the "for" or "while" statement
    print(x)


