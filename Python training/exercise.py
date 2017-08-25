
# 1. This is the print statement
#print("Hello world")

# 2. This is a variable and command to print variable (this varaible is a string)
#message = "Level Two"
#print (message)

#3 You can ask Python what type a variable is.
#print(type(message))


# 4. Another type of variable is an integer (a whole number)
#a = 123
#b = 654
#c = a + b
#print (c)


# 5. You can use other operators like subtract (-) and multiply (*)




# 6. Variables keep their value until you change it
#a= 100
#print(a)
#c=50
#print(c)
#d = 10 + a - c
#print (d)



# 7. You can also use '+' to add together two strings
#greeting = 'Hi '
#name = 'Tim'  # enter your name in this string
#message = greeting + name
#print(message)


# 8. Try adding a number and a string together and you get an error:
age =  65
name = 'Tim'
#print(name + ' is ' + age + ' years old') this produces error. correct shown below

# 9. We can convert numbers to strings like this:
#print(name + ' is ' + str(age) + ' years old')

# 10. Another variable type is called a boolean
# This means either True or False
raspberry_pi_is_fun = True
raspberry_pi_is_expensive = False
#= is an assignment operator
#== is an equality operator
#bobs_age = 14
#your_age = 15
#print(your_age == bobs_age)  # this prints either True or False



# 11. We can use less than and greater than too - these are < and >
#bob_is_older = bobs_age > your_age
#print(bob_is_older)  # do you expect True or False?

# 12. We can ask questions before printing with an if statement
#money = 500
#phone_cost = 201
#tablet_cost = 300
#total_cost = phone_cost + tablet_cost
#can_afford_both = money >= total_cost
#if can_afford_both:
 #   message = "You have enough money for both"
#else:
  #  message = "You can't afford both devices"
#print(message)  # what do you expect to see here?


  

# 13. You can keep many items in a type of variable called a list
#colours = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# You can check whether a colour is in the list
#print('Black' in colours)  # Prints True or False
# You can add to the list with append
#colours.append('Black')
#colours.append('White')
#print('Black' in colours)  # Prints True or False
#print (colours)


# 14. You can add two lists together in to a new list using +
primary_colours = ['Red', 'Blue', 'Yellow','Purple']
secondary_colours = ['Purple', 'Orange', 'Green']
#main_colours = primary_colours + secondary_colours
#print (main_colours)



# 15. You can find how many there are by using len(your_list). Try it below

# How many colours are there in main_colours?
'''
len(primary_colours)# dont work!!!!! use below command
print ('There are ',len(primary_colours),'primary colours')

# 16. You can make sure you don't have duplicates by adding to a set

'''

'''

even_numbers = [2, 4, 6, 8, 10, 12]
multiples_of_three = [3, 6, 9, 12]
numbers = even_numbers + multiples_of_three
print(numbers, len(numbers))
numbers_set = set(numbers)
print(numbers_set, len(numbers_set))
print(set("my name is Eric and Eric is my name".split()))
'''


# 17. You can use a loop to look over all the items in a list

my_class = ['Sarah', 'Bob', 'Jim', 'Tom', 'Lucy', 'Sophie', 'Liz', 'Ed']

# Below is a multi-line comment
# Delete the ''' from before and after to uncomment the block
# Add all the names of people in your group to this list
# Remember the difference between append and extend. You can use either.
# Now write a loop to print a number (starting from 1) before each name
'''
my_class.append('Black')
x = 0
for student in my_class:
    x= x+1
    print(x,student)
'''

#18. You can split up a string by index
'''
full_name = 'Dominic Adrian Smith'

first_letter = full_name[0]
last_letter = full_name[19]
first_three = full_name[:3]  # [0:3 also works]
last_three = full_name[-3:]  # [17:] and [17:20] also work
middle = full_name[8:14]

print (middle)
print (first_letter)
print (last_letter)
print (first_three)
print(last_three)
print(middle+last_three)

'''

'''
# 19. You can also split the string on a specific character
my_sentence = "Hello, my name is Fred"
parts = my_sentence.split(',')
print(parts)
print(type(parts))  # What type is this variable? What can you do with it?
print(type(my_sentence))
my_long_sentence = "This is a very very very very very very long sentence"
# Now split the sentence and use this to print out the number of words
parts1 = my_long_sentence.split(' ')
print(parts1, len(parts1))
# GO! (Clues below if you're stuck)
# Clue: Which character do you split on to separate words?
# Clue: What type is the split variable?
# Clue: What can you do to count these?
'''

# 20. You can group data together in a tuple.Tuples cannot be written to like lists. Theu have () brackets rather than [] like kists
person = ('Bobby', 26)
print(person[0] + ' is ' +str(person[1]) + ' years old')
# GO!


# (name, age)
students = [
    ('Dave', 12),
    ('Sophia', 13),
    ('Sam', 12),
    ('Kate', 11),
    ('Daniel', 10)
]
for stud in students:
    print(stud[0]+' is '+str(stud[1])+' years old')

# Now write a loop to print each of the students' names and age

# GO

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );

print ("subject is  " + tup1[0])
print  (tup2[0:3])




