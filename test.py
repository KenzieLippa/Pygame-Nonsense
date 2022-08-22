print('hello world')

#sublime inserts the code into the python app, 
#can only find cause we have the path files, if not then you would need to add a bunch more
#code executed form top to bottom
#for some reason it prints this perfectly
# print('         __________')
# print('        <          >')
# print('         <        >')
# print('          <      >')
# print('			||	||')
# print('			||	||')
# print('			||	||')
# print('			||	||')
# print('			||	||')
# print('			||	||')
# print('			||	||')
# print('			||	||')
# print('			||	||')
# print('			||	||')
# print('			||	||')
# print('			||	||')
# print('			||	||')
# print('			||	||')

#math section
print(10+5)
print(10 -5)
print(10* 5)
print(10/5)

#exponent
print(10**2)

#floor divide, truncates result basically clips after th decimal
#not rounding because it will make 3.5 into 3
print(7//2)

#modulo, what is the remainder of the division
print(7%2)

#order of operations, pemdas
print((5+5)*2)

# > < =
print(10<5)
#prints boolean

print((1+2+3+4+5+6+7)/7)

#variables
result = 1+2
print(result)

result2 = result/2
print(result2)
#can only contain letters numbers and underscore
#NO spaces or $, %, also cannot start with a number
#cannot be named after a python keyword
test_1_A = 'test'
#2test = 'test', cannot do
#use snake_case, all lowercase and use the _ to connect to the next word
#variable names should not be vauge and should be consistant
testNum = 1
testNum +=2
testNum *=10
testNum /=2
print(testNum)

snake_case = 2
snake_case +=20
print(snake_case)

#functions
#print, len, abs
print('argument')
print(len('how long is this?')) #prints number of characters (counts space)
math = abs(-50)
print(math)
print('one argument', 'another argument', 'accepts ulimited arguments')

#selects the largest argument we passed in

max1 = max(0,10, 2,3 ,4)

min1 = min(0,1,2,3)
print(max1)

#methods are attached to objects
word = 'a word'.upper()
#can also be applied to the variable
print(word)

username = 'jOhn smIthXX'
#can use methods to clean things up
#title things turns it into title case, 
#stip gets rid of some specific stuff
username.title().strip('x')
#dir tells you the methdos that can be used on the current object
#print(dir(username))
#keep working and look things up and then you learn them
#are there numbers in your word
print(username.isalpha())

excersize_string = 'I like puppies'
excersize_string.replace('puppies', 'Cleo')
print(excersize_string)

#return
#every option returns a value
test_variable = len('A word'.upper().replace('A', 'X'))
#how many characters within th function
#replaces the a with an x
#returns a word all uppercase
#print(print()) returns none
print(print(test_variable))

#comments
#really useful for organizing and then also telling what happens
#ignore me
'''this is the other comment but its not quite a comment but it can be used as one
this also allows you to have something on multiple lines
dont forget ctrl / to comment out chunks'''

#execution order
#doesnt see enters/ lines with no code in it
#white space shows up in ''
#white space next to code so 1+2 is th same as 1 + 2
#DOES care about indents
print(   '   A '  )
#can use semicolon to break into one physical line
#if you have \ it then links togeter
print('1'); print('2')
a = 1+2+3+4+5\
+6+7+8


#data types
#string
#int, float
#boolean
#list, can store other values
#tuple is like a list but cant be changed
#set all values have to be different
#dictionary name: data type

#type tells what type value is
#all division gives u floats
print(type(1.1))
print(float(2))
print(int(2.1))
print(round (0.9))

print(1.1*3) #computers r weird, try to avoid floating point numbers

#strings
test_var = 'test1'
test_var2 = "test2"

print(test_var, test_var2)

#quotes in strings
# test_Var3 = 'He said 'this was great''
#ok with mixing quotes
test_var3 = "he said 'This was a good time' "
test_var4 ='\"\'' #escape characters, characters to tell python to just print it and not read it in
test_var5 = 'Line 1: some text \n or \r or theres the tab \t Line 2: some more text'

#multiple lines
test_var6 = '''all the line 
breaks 
will be perserved
otherwise this wld be a comment but its not bc its assigned to a value'''

test_var7 = 'hello' + ' '+ "World"
#python doesnt care about ' ' vs "" as long as they match
test_var8 = 'copy '*8
#prints copy 8 times

name = 'bob'
age = 40
greeting_string = 'hello {}, you are {} years old.'.format(name,age)
#looks for first {} and replaces it with whats in index 0, in index 1 places in second {}
#can also put htings in the brackets
greeting_string1 = 'hello {name}, you are {age} years old.'.format(name = name,age = age)
print(greeting_string1)
#formats with f
greeting_string_improved = f'hello {name}, you are {age} years old.'
print(greeting_string_improved)

x = 'kenzie'
y = 'art'
test_string = f'Hello, my name is {x} \n and my hobby is {y}'
print(test_string)


#tuples and strings
#tuples(1, 'test', True, ('another tuple'))
#list[1, 'test', True, [list]]
my_list = [1,2,3,4,5, 'word']
print(my_list)
#can also use len
len(my_list)
#deletes all values
my_list.reverse()
#add a value to the end
my_list.append(10)

my_tuple = (1,2,23,4,5,'Word', [1,23,4])

#how to pick elements from a list or tuple
#indexing and slicing
#counts fom 0 not 1
print(my_list[0])
#hits the list
print(my_tuple[6][0])
#negative numbers start at the back of th list

my_list.clear()

excersize_list = ['first nonsense',[123,456,[0,'Hello :)']], 'bye']
print(excersize_list[1][2][1])

#slicing
#[start:finish] but doesnt include the end
test_list = [1,2,3,4,5,6,7,8,9,10]
print(test_list[1:3])
#can add a third value to indicate step size and direction
print(test_list[1:8:2])

#can reversed
print(test_list[-1:4:-1])

#every value has a default value, start is usually 0 end is usually the end and th step is 1
default_slicing = test_list[::2]
print(default_slicing)
#can also just do [::] for all values
test_excersize = test_list[7:0:-2]
print(test_excersize)

#tuples nonsnese
test_tuple = [1,2,23,4,5,6,7]
print(test_tuple[1:4:2])

#unpacking
a,b = (10,5)
c,d = [10,4]

#need as many variables as the tupple
#values with comas are tuples

f,g,h = 1,2, 'sword'
value_1 = 10
value_2 = 'test'
value_2, value_1 = value_1, value_2

test_string1 = 'this is a test'
test_list = [1,2,3,4]

#turning a string into a list/tuple
test_string1.split() #if specify value then splits by that and removes it
#turn into a list
print(list(test_string1))
print(tuple(test_string1))

#turn a list/tuple into a string
#what ever in the ' ' is whats in between all the values in the list
#everything in the list has to be a string tho
print(' '.join(['one', 'two']))
#looks like if u just printed th list but does actually change it into a string
print(str(test_list))

#Indexing a string, string is just a container for letters
print(test_string1[0:5])

print(str(test_list).replace('[',' ').strip(']').replace(',',''))

#dictionary

test_dict = {'key': 123, 'B': [1,2,3], 1: True}
#dont use the same keys, second key overwrites the original
print(test_dict.values()) #can also put in type and figure out
print(test_dict.keys())
print(test_dict.items())
print(len(test_dict))

print(list(test_dict))
print(str(test_dict))
#indexing does not work
#looks for key and returns the value assosciated with it
print(test_dict['B'])
print(test_dict.get('X'))#doesnt crash if doesnt find key

#update the dict
test_dict.update({'Keys': (1,2,3)})
test_dict.update(C = 'test', D = '123')
test_dict['E']=100
print(test_dict)

#sets
#has to be unique, {} without the keys
my_set = {1,2,3,4}
print(len(my_set))
my_set.add(5)
my_set.remove(1)
#can easily look up the methods you can use with it

#indexing and slicing does not work
print(my_set.pop())
print(my_set)
#prints out th first but then deletes it
#change data type for this single purpose and then it stays th same
print(list(my_set)[0])

#used as comparison operators
set1 = {1,2,3,4,4}
set2 = {4,5,6,7}

print(set1.union(set2)) #mix them both together
#other way to write
print(set1 | set2)

print(set1.intersection(set2))#only print the value they share
print(set1 & set2)


print(set1.difference(set2)) #only get the values not in set2
print(set1-set2)

test_list1 = [1,2,3,4,5,4,6,6,7,6,88,5, 6,7,8,9,99,0,0,3,4,5,6,6,6,6,6,3,3,3,3,2,2,4,4,4,42,42,42,4,233,4,4]
print(len(test_list1))
#if you turn it into a test list how much shorter is it, thats the number of duplicates

print(len(set(test_list1)))
#returns false if there are duplicates
print(len(test_list1)) == len(set(test_list1))

	#booleans
	#comparison operators
	# == is equal, != not equal
	#<= less than or equal
print(1==1)
print(1!=10)

print(1<=10)

#list and booleans
print(1 in [1,2,3])
print('e' in 'hello')
print(4 not in [1,2,3])
#not reverses any boolean

#boolean by self
print(not True)

#data conversion
e_dict = {1: 'one', 2: 'two', 3: 'three'}

#dont actually need the .keys for this one to check to see if its here
print(1 in e_dict.keys())
#this one definitely needs the .values cause e_dict only counts the keys by default
print('four' in e_dict.values())

#bool() can accept any number string type or container and get a value from it

#truthy- values that are converted to true
#falsy- values that are converted to false
#any 0, empty string, empty list tuple set or dictionary and None. everything else true
print(bool(123123123123123))
print(bool(0))

#if statements
#looking for a boolean 
print(10>5)
x1 = 5
if x1 > 10:
	print('the if statment was true')
	#i wish this was faster
elif x1!= 0:
	print('the elif statment was correct')
	#as many elifs as you want but only one if for each else in each block
else:
	print('this statmenet was false')

money_available = 100
if money_available >= 80:
	print('eat something fancy')
elif money_available > 45:
	print('eat something nice')
elif money_available > 15:
	print('eat something ok')
else:
	print('eat something cheap')

	#combining conditions
	if 5 < 1 and 'e' in 'hello' or 10 <4:
		print('true')

	#combines all blocks in and 
money_available1 = 100
hungry = True
bored = True
if money_available1>80 and hungry == True or bored == True:
	print('eat something fancy!')
x = '1'
#nesting if statements
if 'a' in ['a', 'b']:
	print('a is in th list')
	if x.isalpha():
		print('it is a letter')

	if True:
		print('something')

if money_available > 80:
	print('I have enough money!')
	if hungry == True:
		print('and i am hungry')
		if bored == True:
			print('eat something fancy:)')

#switch statements/ match cases

mood = 'salty'

if mood == 'hungry':
	print('get some food')

match mood:
	case 'hungry':
		print('get food')
	case 'thirsty':
		print('get water')
	case 'salty':
		print('yell at ray ;P')

#excersise
grade = 1

#no breaks and also _ is for default
match grade:
	case 1:
		print('very good')
	case 2:
		print('good')
	case 3:
		print('okay')
	case 4:
		print('needs improvement')
	case 5:
		print('very bad')
	case _:
		print('very bad')

#while loops
#only runs while trie
x2 = 0
while x2<10:
	print(x2)
	#iterators
	x2+=1
	if x2==5:
		# when its 5 then stop
		#break
		#continues and skips th rest of th loop
		#wont print 5
		continue
	print(x2)


my_list1 = []
counter = 0
while counter <= 100:
	
	if counter % 2 == 0 and counter != 58:
		my_list1.append(counter)
	
	counter +=1
	print(counter)
	

print(my_list1)

#for loop
for x in [1,2,3]:
	print(x)
basic_list = [1,2,3]
for x in basic_list:
	print(x)
	#runs for every item in list
	#in loop do something for th object
	#tuples and sets work th same as sets
	#for dict get th keys and .values() or .items() to get th items and keys
	#needs an iterable and not just an int
	#range(3)
	for x in range(3):
		print(x)
		#range goes from 0-3 but doesnt include it
		#can have start, end, step
		practice_list = [[10,40,20,50], [2,42,10], [101,10,4]]

for x in practice_list:
	temp_list = x
	print(temp_list)
	for y in temp_list:
		if y > 10 and y <50:
			print(y)


for nested_list in practice_list:
	#print(nested_list)
	#value takes the list and saves it as its value
	for value in nested_list:
		if value > 101:
			break
		if value <50 and value>10:
			print(value)

#flow and line breaks
#on one line no colon
grade = 1 if money_available == 100 else 5
x3 = 1
#true value if expression else false value
print(f"the color is{'red' if x3 < 5 else 'blue'}")

a = ['red' if x3 <5 else 'blue', 'yellow', 'green']

#functions
#1. create the function where th codes added
#2. call th functions and execute th code

def test_function():
	print('hello')
	test = 1+2
	print(test)

def calculator(num1, num2):
	result = num1 + num2
	print(result)

test_function()
test_function()
calculator(2,3)

def better_calculator(num1, num2, func):

	result = 0
	match func:
		case 'plus':
			result =num1+num2
			print(f'{num1} + {num2} = {result}')
		case 'minus':
			result = num1-num2

		case 'divide':
			result = num1/num2
		case 'multiply':
			result = num1*num2
		case 'exponent':
			result = num1**num2
	


better_calculator(1,2,'plus')
#parameters have no relation to other parameters

#parameters
#in () for func and first is first and second is second

def test_func(arg1, arg2, arg3 = 'key'):
	#default argument
	print(arg1)
	print(arg2)

#can put in positions or also can put th names in front so you know what goes to what
test_func(arg1= 1, arg2 = 2)

#position arguments have to go before all the others

def greetings(person, greet, weekday):
	print(f'Hello {person} {greet} Today is {weekday}')

greetings('Ray', greet = 'How are you today?', weekday ='Thursday')

#what if u dnt know how many arguments
def print_all(arguments):
	for argument in arguments:
		print(argument)

#list unpacking
def print_all2(*arguments, extra):
	#doesnt know by default when unpacking ends so you need to use a keyword for th last term
	#looks at everything passed in and creates a tuple
	print(arguments)
	print(extra)

#keyword unpacking
def print_more(**arguments):
	print(arguments)

print_more(arg1 = '1', arg2 = 'test', arg3 = [1,2,3])
#returns as a dictionary 

def print_even_more(*args, **kwargs):
	#tuple
	print(args)
	#dictionary
	print(kwargs)

def unlimited_calc(*nums):
	sum1 = 0
	for num in nums:
		sum1+=num
		#or theres sum which is faster
	print(sum1)

unlimited_calc(1,2,3,4,5)

#local and global scope
a = 10

def test_funct():
	#cannot do a+=2, when creating func all variables are not connected
	#all vars only exist in the funct
	#fine
	print(a)

	#helps with variable names
	#every func has own scope and is all seperate

def scope():
	scope1 = 'we exist in here'
	print(scope1)

def test_func_3(a):
	#global a 
	a += 2
	print(a)
	return a
#update a after function
a = test_func_3(a)

multiplier = 10
has_calculated = False

def mult_calc(number):
	#can use values from global but can not update
	result = number * multiplier
	global has_calculated
	has_calculated = True
	#ends th function so has to go at th bottom
	return result

print(mult_calc(2))

#lambda functions, for simple functions, saved to a variable
z = lambda x: x+1
simple_calc = lambda a,b: a+b
print(z(2))

#some functions want other functions as arguments

#sort([1,2,3], func) tells it how to sort th numbers
#graphical user interfaces
#basic shit when a button is pressed
#auto returns value
more5 = lambda x:'hello' if x>5 else 'bye'

#explaining what th func does
#add some doc string or a hint
#looking for an int for both
# -> tells return value
def doc(a:int = 10,b:int = 0) -> int:
	'''A simple func tht prints th 2 parameters'''
	print(a)
	print(b)
	return a + b

print(doc.__doc__) #doc string
help(doc)

#data operators

#manipulate lists to get stronger loops
inventory_names = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrivers', 'Wood']
inventory_numbers = [43,12,95,421,23,43]

#wants two lists
#can convert into list
list(zip(inventory_names, inventory_numbers))

for thing in zip(inventory_names, inventory_numbers):
	print(thing)
	#[0] for names [1] for numbers
	#creates a touple with both connected
for name, number in zip(inventory_names, inventory_numbers):
	#assigns first to name and second two number
	print(name)
	print(number)

#enumerate func
#get current index
#convert to list for reading purposes
print(list(enumerate(inventory_names)))
for index, name in enumerate(inventory_names):
	print(f'{index}: {name}')
	if index == len(inventory_names)//2:
		print('halfway done!')

def inventory(names, number):
	for index, nameList in enumerate(zip(names, number)):
		
		print(f'{nameList[0]} [id:{index}] - inventory: {nameList[1]}')

inventory(inventory_names, inventory_numbers)


#list comprehension
#put all values from 0-100 
#can use ternarys but if its second cant add else
my_list2 = [num for num in range(0,100) if num <10]
#can also do for other way around
my_list3 = [num if num <10 else 0 for num in range(0,100)]
my_lists = [num for num in range(0,100)]

replenish_list = [(name, number) for name, number in zip(inventory_names, inventory_numbers) if number < 25]

#combine list comprehension
#can put x and y in a pair and it will take ys value and xs value
combined_comp = [[(x,y) for x in range(5)] for y in range(10)]
#get multiple lines, created this inner list 10 times
for row in combined_comp:
	print(row)

chess_board = [[f'{letter}, {number}' for number in range(1,9)] for letter in'ABCDEFGH'[::-1]] #use the slicing [start, end, step]
for row in chess_board:
	print(row)

#comprehension for other datatypes as well
#works for dicts and sets
dict_comp = {num: num for num in range(10)}
set_comp = {num for num in range(10)}
tuple_comp = tuple(num for num in range(10)) #need th tuple keyword

set_com = {num for num in range(100)}
print(set_com)
dict_com = {num: num for num in range(100)}
print(dict_com)

tuple_com = tuple(num for num in range(100))

#excersize
chess_dict = {key: [1,2,3,4,5] for key in 'ABCDE'} #key is whats being changed, value stays the same
print(chess_dict)

funList = [4,2,3,1,5]
#reverse is a parameter in sorted
print(sorted(funList, reverse = True))
funList.sort() #also sorts it
listBad = [('a', 3), ('b',10), ('c', 6), ('d', 5)]
def sword_func(item):
	return item[1]

print(sorted(listBad, key = sword_func)) #dont call th function
#know what to look for inside the item, has to return an integer with th function
print(sorted(listBad, key = lambda item: item[1])) #use lambda in order to write funcs info 
combined_list = list(zip(inventory_names, inventory_numbers))
sorted_comp_num = sorted(combined_list, key = lambda inv_tuple: inv_tuple[1])

sorted_comp_name = sorted(combined_list, key = lambda inv_tuple: len(inv_tuple[0]))

#ok i kinda think i know how this works?
#map
my_map = [1,2,3,4,5]	
#map changes values with a function inside of a iterable

#map(key, iterable)
#passed into th fucntion as a value
def power_function(num):
	return num ** 2

map(power_function, my_map)

print(list(map(lambda num: num **2, my_map)))
#filter - filters out values from a condition
def get_below_4(num):
	if num <4:
		return True
	else:
		#if returns false then they get filtered out
		False
print(list(filter(get_below_4, my_map)))

print(list(filter(lambda num: num <4, my_map)))

#list comprehension is for trying to make the function without using it.
print([num **2 for num in my_map])
print([num for num in my_map if num <4])
