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

file = open('Test.txt')
print(list(file))
#want to close the file as well
file.close() #removes out of memory to make more efficient

#open and close auto
with open('Test.txt') as file:
	#opens the file and then use it here, once over then close automatically
	print(file.read())#converts to something we can use more easily
	#is a string, if u list u get the characters
	for line in list(file):
		print(line)
		#print all lines from file

	#write file, 'r' is the auto then 'a' is for append and 'w' is for right
with open('Test.txt', 'a') as file:
	file.write('\nxxxxxxWrite some more text xxxxxxx')


with open('tree.txt', 'w') as tree_file:
	tree_string = '''
	  x
	 xxx
	xxxxx
	  x
	  x
	  x
	  x
	'''

	tree_file.write(tree_string)
#only need to delete values from a list most of the time
weirdVal = 1
del weirdVal
#deleted the variable

#remove items from a list
weirdList = [1,2,3]
del weirdList[1]
print(weirdList)

#remove the item by value
weirdList.remove(3) #remove the value uve written in here.

#can also use the pop
weirdList.pop() #pops out th value deleted and is saved, default index is -1

weirdList.clear()#clears the list.

#classes
#objects: container for variables and functions
#make a video game with monsters and have health energy damage, needs to move animate and fight
#variables are only available in the container
#variables in an object are an attribute, functions are methods
#can have multiple objects
#each object has its own attributes and methods, objects can also interact with each other
#organize via different objects for object-oriented programming


#what are classes? a blue print for an object
#can accept arguments to customize the object

#one class can inheret from other classes as well

#organize complex code and create reusable code, help create reusable code
#make easier to work with scope
class Monster:
	#attributes, but i want custom values
	#dont need these until the init method
	# health = 100
	# energy = 40
	'''monster that has some attributes '''
	def __init__(self, health, energy):
		#the heath parameter and the input
		#two member variables
		self.health = health
		self.energy = energy
		print('the monster was created')

		#private attributes
		self._id = 5 #should not be worked on but can be worked on

	def __len__(self):
		#return something
		return 5
	def __abs__(self):
		return self.energy #can do what ever you want with this
	def __call__(self):
		return 'the monster was called' #if you add brackets afte rmonster this will get called
		#can also just print tht
		print('the monster was summoned')

	def __add__(self, other):
		return self.health + other

	def __str__(self):
		#dunder string, returns some text (i remeber working with this)
		return 'A monster'
		#call with str or just with print
	def attack(monster, attack):
		#first parameter always refrences the object created by the class
		print('The monster has attacked!')
		print(f'{attack} damage was dealt!')
		monster.energy -= 20 #because the object is th first parameter it is able to modify variables in the class
		print(monster.energy)
#first is usually self
	def move(self, speed):
		print(f'The monster moved at {speed} MPH!')
#turn class into object
monster = Monster(10,20) #capture object in a variable
monster2 = Monster(health = 20, energy = 100)

print(monster.health) # health is only in the class and accessed with object.variable 
#monster.attack() doesnt work, says that theres a issue
#passes in the object default into the functions in the func in th class

monster.attack(10)
monster.move(20)
print(len(monster)) #links to th len method
print(monster + 55) #can add to the monster in the parenthesis
#dunder methods
#dir prints result of the object
#many dunder methods are made automatically and u dont have to say them
#__dict__ returns the values as a dictionary, can also use vars
#called by python when something else is happening
#func is len(test) method is test.upper() only on string

testvar = 'a'
print(dir(testvar))

def testFun():
	pass
#func is an object with th dunder call
ass = testFun

ass.another_attribute = 100

def add(a,b):
	return a+b

class Test:
	def __init__(self, add):
		self.add_function = add
#passed in the function add for this parameter that we created earlier
test8 = Test(add = add)
#mind fuck nonsense
print(test8.add_function(1,2))
class Monster2:
	def __init__(self, func):
		self.func = func


class Attacks:
	#good way to organize functions
	def bite(self):
		print('IVE BIT YOU')
	def strike(self):
		print('Ive struck you!')
	def slash(self):
		print('I got a knife and imana cut you')
	def kick(self):
		print('ive kicked you')

attack = Attacks()
monster3 = Monster2(attack.bite) #can also call Attacks().bite
monster3.func()

#classes and scope
#every method has a refrence to the class, because of this its easy to get and change class attributes
#rely less on parameters, global and return
#objects can change outside the local scope

class Monster3:

	def __init__(self, health, energy, **kwargs):
		print(kwargs)
		#keyword unpacking, save any extra parameters you get into a kwargs dictionary
		self.health = health
		self.set_energy #can use with the return parameter
		#call the super init method here
		#follows the inheretance set by the shark, th init method wont do anything if called alone from just monster
		super().__init__(**kwargs) #puts in the extra variables in as a named argument
		#this method will work for what ever uve passed it and what ever the next class is so if its fish then you pass fish init values and if monster
		#dettects them then they will go in the kwargs and be read into the fish method
	def update_energy(self, amount):
		#select attribute and update it to what ever you want
		self.energy += amount

	def set_energy(self, energy):
		new_energu = energy *2
		self.energy = new_energu
		return new_energu
	def getDamage(self, amount):
		self.health -= amount

def update_health(amount):
	monsterN.health += amount #can update an object anywhere


#onsterN = Monster3(100,59) 

#create hero class with 2 parameters

class Hero:
	def __init__(self, damage, monster):
		self.damage = damage
		self.monster = monster

	def attack(self):
		self.monster.getDamage(self.damage)


# class MeanMonster:
# 	def __init__(self, health):
# 		self.health = health
	

squid = Monster3(100, 50)
fred = Hero(10, squid)
print(squid.health)
fred.attack()
print(squid.health)

#inheritance
#can get complex, can inheret from other classes
#gets info from parent class
#to inherit then you put the parent in parenthesis
class Shark(Monster3):
	def __init__(self, speed, health, energy):
		self.speed = speed #new attribute
		#need to call the init method from th 
		#self wld be monster but is now refering to the shark
		#Monster3.__init__(self, health, energy)
		#gets parent class
		super().__init__(health,energy)

	def bite(self):
		print('the shark has bitten!')

	#override a method, define a same method 
	def move(self):
		print('The shark has moved')
		print(f'The speed of the shark is {self.speed}')

class Scorpion(Monster3):
	def __init__(self, poison, health = 100, energy = 90):
		self.poisonDamage = poison
		#only gets these attributes if u add this info, can also set static numbers in here
		super().__init__(health, energy)

	def attack(self):
		print('The Scorpion has attacked!')
		print(f'it has dealt {self.poisonDamage} poison damage!')

shark = Shark(speed = 129, health = 100, energy = 80)
print(shark.health)
shark.move()
scorpion = Scorpion(10)
scorpion.attack()
class Fish:
	def __init__(self, speed, scales, **kwargs):
		self.speed = speed
		self.scales = scales
		super().__init__(**kwargs)

	def swim(self):
		print(f'the fish is swimming at the speed of {self.speed}')


class Shark2(Monster3, Fish):
	def __init__(self, bite_strength, health, energy, speed, scales):
		self.bite_strength = bite_strength
		#how to do the super cause theres two instead of one
		#mro->method resolution order
		#left most is the first, shark is 0, then 1,2
		#super is the first item in 
		#need the keyword equals part in here
		super().__init__(health = health, energy = energy, speed = speed, scales = scales)
		#fish inheretance is not working rn, no one called the fish init method, needs arguments inside the fish too
print(Shark2.mro())

#complex inheretance
#before you have parent class and child, but you can also have multiple parents
shark3 = Shark2(bite_strength = 50, health = 200, energy = 55, speed = 120, scales = False) #python knows th first item of inheretence

#private attributes
'''private can not be changed outside of the class, not mess with other code'''


#hasattr and setattr
#hasattr(object, 'attribute name')
if hasattr(monster, 'health'):
	#if monster has the attribute health then print this statement
	print(f'the monster has {monster.health} health')
#setattr(object, 'attribute', value)
setattr(monster, 'weapon', 'Sword') #added and set the attribute
monster.weapon = 'Sword'#also sets the attribute

new_attributes = (['weapon', 'Axe'], ['armour', 'Shield'], ['potion', 'mana'])
for attr, value in new_attributes:
	setattr(monster, attr, value)
	#set a lot of them with this all at once, probably wld wanna create all of these when u make the object tho


#doc string
#explains everything
print(monster.__doc__)
help(monster) #can see all the info about the method and all of the stuff it has, can use this for any object or keyword


#modules
'''kind of like libraries
can create own module and also can use other peoples modules for extra functionality
can import from the standard library, pre-installed with python
can use additional modules made by others to help.'''
import string 
from math import floor as get_floor #renamed the function and imported only floor from the math function
from random import * #all methods and functions for random without having to write random first
from datetime import datetime as dt #have one object called datetime
import pyautogui #automates windows to a certain extent
from time import sleep

random_num = randint(0,10) #random integer, can call it, needs min and max
print(random_num)
#google the module and it will show you everything that the module has
test_list2 = [1,2,3,4,'Ray',[1,2,3]]
choice(test_list2) #will pick a random value from the list
#python standard library will also show you this stuff
print(string.ascii_lowercase)
#print(math.sin(1))
print(get_floor(4.9))#round down
#google a problem and find the solution
print(dt.now())

#external modules
#made by other programmers
#also need to be installed in python first
#pip install and uninstall
#sleep(1) #wait a second
#pyautogui.write('This is written by a computer... I know where you live and I am coming to find you. You arent safe anymore...', interval = 0.25) #interval duration between
#fun module where you can do a bunch of nonsense
#pyplot and try to follow examples
import sys
import matplotlib.pyplot as plt
print(sys.executable)

plt.plot([1,2,3,4, 10, 0, 100])
plt.ylabel('some numbers for the y axis')
plt.xlabel('fancy unicorns')
plt.show()
#can also create custom modules
