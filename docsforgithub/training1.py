""" just giving computer tasks to carry out 
- drawing a little triangle """


# print("   /|")
# print("  / |")
# print(" /  |")
# print("/   |")
# print("-----")
# # variable = container for data{ to manage data for our program}
# # variable for name and age
# # control and manage data 
# # manage values in the code with variables 


# character_name = "Fredrick"
# character_age = "30"

# story = ("There was once a man called:  " + character_name + " who was:  " + 
# 	character_age + " years old,  and loved soccer so so much")
# print(story)


#type of data to store in variables 

#1)  sting = plain text ( name = tom)
#2)  numbers = age =50 --also floats 
#3)  Boleen value ( True or False i.e  is_Male = True  or False)
#4)_-----------------------------------------------------------------

#working with strings in python 
# ( plain text ) 

# print("Fredrick \rMangidi") #start newline
# print("Fredrick \nMangidi") # start newline 
# print("Fredrick \"Mangidi") #-add quatation mark 
# print("Fredrick \Mangidi")  # backslash 

# # # string variable 
# phrase  = "Jacob  Dangidi"

# print(phrase)
# #concatenation 

# print(phrase + " is cool")

#functions 
#- little block of code to execute code for us 

# print(phrase.lower())
# print(phrase.upper())

# check if upper or lower 
# print(phrase.isupper())
# print(phrase.isupper())
# print(phrase.upper().isupper())

# print(len(phrase))
# #-individual characters 
# print(phrase[0])
# #String get indexed starting with zero 
# print(phrase[0:3])
# print(phrase[3])

#index function - find where character is located in the function
# give it a perameter  
# print(phrase.index("J"))
# print(phrase.index("Dangidi"))

# # replace characters 
# print(phrase.replace("Dangidi", "Babazolla"))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# numbers most common types of data and types of numbers 
#- functions with numbers 
#-specify order of operations 
# #----------------------------------------------------------
# print(2) 		#whole number 
# print(2.345) 	# float 
# print(3+ 4.5) 	# addition/sub/multi/ 
# print( 3*4 + 5)
# print(3 * (4 + 5)) # change order 
# #modular operator (ten mode 3)
# print(10 %3)   # gives us the remainder ( of 10 /3 )

# store in variables 
my_num = 5
# print(my_num)

# # convert to string { convert to string }
# print(str(my_num))

# print(str(my_num) + " My favorite Number ")

# maths functions and operators : 
#------ABS - Absolute  Value of a number 

# print(abs(my_num))

# num2 = -5 
# print(abs(num2))

# #pow ( need 2 info ( number & power ))
# # ie 3 raised to power 3 (3^3)
# print(pow( 3,2))

# print(max( 3,6))  # bigger number 
# print(min( 3,2))  #minimal number 
# print(round( 3.2)) # rounbd it to normal (3)

##############################
# importing math functions (math module) 

# from math import * 

# mydigit = -4 
# print(floor(3.7)) # floor chops off number after decimal points 

# print(ceil(3.7)) # floor rounds the number up 
# print(sqrt(36)) # square root of a number 


# getting input from users (into our program and store it and use it 
#INPUT OUTPUT )
#-----------------------------------------------------------------
# name = input(" Whats your name:  ")
# #print("Good morning : {} !".format(dada))
# print("Hello " + name + "!")



#################################
 
# num1 = input("Enter a number : ")
# num2 = input(" Enter another number: ")
# result = int(num1) + int(num2)
# result2 = float(num1) + float(num2)
# print (result)
# print (result2)


# # app.get("/", (req, res) => {
# # 	res.send['Hello world']
# # 	})
# app.listen(port, {} => {
# 	console.log('Listening at port: ' + port)
# 	})


################################
# lists 

# friends = ["kelvin", "Kaloo", "Jopa", "Allan", "Kaka", "Ronaldo"]
# print(friends)
# print(friends[0])
# print(friends[1])
# print(friends[2])
# #----------
# print("------: -1" + friends[-1])
# print("------: -2" + friends[-2])
# print("------: -3" + friends[-3])


# print("+++++++++++++++++++++++++++")
# print(friends[:1])
# print(friends[1])



# append to a list 
# lucky_numbers = [1,2,3,4,5,6]
# friends = ["kelvin", "Kaloo", "Jopa", "Allan", "Kaka", "Ronaldo"]

# # add two lists together 
# friends.extend(lucky_numbers)
# print(friends)

# # append 

# friends.append("creed")
# print(friends)

# # insert element into a string ( everything gets pushed to the right )
# friends.insert(1, "Robbo")

# print(friends)

# # remove elements 
# friends.remove("Robbo")
# print(friends)

# clear the list 

# #print(friends.clear())
# #use pop off the list (last element )
# print(friends.pop())

# check if something is in 

# print(friends.index("Ronaldo"))

# #how many times an element is present 
# print(friends.count("Ronaldo"))

# print(friends.sort())


# lucky_numbers = [1,2,3,4,5,6]
# friends = ["kelvin", "Kaloo", "Jopa", "Allan", "Kaka", "Ronaldo"]

# print(friends)
# print(lucky_numbers.sort())
# dir(friends)


######################
# tuples  - data structure  
# - cannot be changes once created 
# - 
##########################
#- UNIQUES - IMMUTABLE ( Cannot be changed or modified, change erase -- nothing else )
# once created thats it --period
# coordinates ( OPEN ANC LOSE PARENTHESIS ())
#- they are index starting from zero
# # data tyhat cannot be changed or mutated 
# coordinates = (4, 5) 
# #- coordinates[0]
# print(coordinates[0])


#_______________________________
# # functions 
# #-------------------------------

# def tester(hi):
# 	#print(tester())
# 	#return f" Nice meeting you {tester}"
# 	print(f" Nice meeting you {hi}")

# message="Shikamoooo"
# tester(message)

# def tester2(fast_name, last_name):
# 	print(f"My name is {fast_name} : {last_name}  and I love soccer")
# 	#return "My name is : {}, {}".format(fast_name, last_name)

# fastname= "Mangidi"
# lastname = "Mweshimiwa"
# tester2(fastname, lastname)


# # pass in str 

# def tester3(name , age):
# 	print(f"My name is {name} : {age}  and I love soccer")
# 	#return "My name is : {}, {}".format(fast_name, last_name)

# fastname= "Mangidi Mweshimiwa "
# old = "50"
# old2 = 50 

# tester3(fastname, old)
# tester3(fastname, old2)


#------------------------------------
# return function 
# - get information from a function 
#------------------------------------

# def cube(num):
# 	return num*num*num 


# result = cube(4)  # stores value that got returned 
# #print(cube(3))
# #- print(caller)
# print(result)


#------------------------------
# if statements 
#-----------------------------------------

# is_male = True 

# if is_male:
# 	print("You're a male champ")

# is_female = False

# if is_female:
# 	print(" Women are beutiful always")
# else:
# 	print("Sorry I was looking for a female champ")


# is_male = True
# is_Tall = False

# if is_male or is_Tall:
# 	print(f"Your are a Tall man")
# else:
# 	print("You're neither male nor tall")


# if is_male and is_Tall:
# 	print("Yess: you're both male and Tall")
# elif is_male and not (is_Tall):
# 	print(" you're male amd not tall ")
# elif not (is_male) and is_tall:
# 	print("Youre not male but Tall")
# else:
# 	print("Youre not male and not tall")


# #########################################
# #max 

# # 
# def max_num(num1, num2, num3):
# 	if num1 >= num2 and num1 >= num3:
# 		return num1
# 	elif num2>= num1 and num2 >= num3:
# 		return num2 
# 	else:
# 		return num3

# print(max_num(3,4,10))
# print(max_num(44,4,22))



#####################################
# DICTIONARY 
#key value pairs 
#_____________________________________
#- Access key value pair from inside the dictionary 
# # -

# monthConversions = {
# 		"Jan" : "January",
# 		"Feb":  "February",
# 		"Mar": "March",
# 		"Apr": "April",
# 		"May": "May",
# 		"Jun": "June",
# 		"Jul": "July ",
# 		"Aug": "August ",
# 		"Sept":"September",
# 		"Oct": "October",
# 		"Nov": "November",
# 		"Dec": "December ",
# }

# print(monthConversions["Nov"])
# print(monthConversions.get("Dec"))

# # default value for missing value 
# print(monthConversions.get("Luv", "Not a valid key"))


#---------------------------------------------
# while loop 
#-----------------------------------------------

i = 1 

while i <= 10:
	print(i)
	1 += 1 

print("Done with loop")





secret_word = "giraffe"
 guess = ""
 guess_count = 0
 guess_limit = 3
 out_of_guesses = False

 while guess != secret_word and not (out_of_guesses):
 	if guess_count < guess_limit:
 		guess = input( "Enter Guess: ")
 		guess_count += 1
 	else:
 		out_of_guesses = True

if out_of_guesses:
	print("You lost the game")
else:
	print("You win")



##################################
# class= Overview what the actual data type is 
OBJECT ==> IS an instance of a class  

class Student:
   def __init__(self, name, major, gpa, is_on_probation):
   	self.name = name 
   	self.major = major 
   	self.gpa = get_emplos_by_nameself.is_on_probation = is_on_probation 






# oBject is the actual student we're creating 

from students import Student 

student1 = Student("Jim", "Business", 3.1, False)

print(student1.name)
print(student1.gpa)

# student stores all the information as an attribute 




class Question:
	def __init__(self, prompt, answer):
		self.prompt = prompt
		self.answer = answer 



#####################################

from Qquestion import Question

question_prompt = [
"What color are apples? \n(a red/Green \n(b) Purple\n(c) Orange\n\n", 
"What color are Bananas? \n(a) Teel\nb) Purple\n(c) Orange\n\n"


]
#questions Object 

questions = [

Question(question_prompt[0], "a"),
Question(question_prompt[1], "b")


]

def run_test(questions):
	score = 0
	for question in questions:
		answer = input(questions.question_prompt)
		if answer ==  question.answer:
			score  +=  1

	print("You've got " + str(score) + "/" str(len(questions)) + "Correct")



####################################

# instance variables 
#- instance self 

class Employee:
	raise_amount = 1.04 

	def __init__(self, first, last, pay, email):
		self.first = first
		self.last = last 
		self.pay = pay 

		self.email = first =+ '.' + last + "@company.com"


		def  fullname(self):
			return '{} {}'.format(self.first, self.last)



		def apply_raise(self):
			self.pay = int(self.pay * Employee.raise_amount)

	

	empl_1 = Employee('Fredrick', 'Were', 5000)
	


print(empl_1.email)
print(empl_1.email)
print('{} {}'.format(empl_1.first, empl_1.last))
print(empl_1.funllname())  # method need parenthesis ( its not an attribute 
#- with class itself 

Employee.fullname(empl_1)



#__________________________________________________
# calling parent init methods 
def Developer(Employee):

	raise+amnt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(fast. last, pay)
		# OR CALL FROM CLASS
		Employee.__init__(self, first, last, pay)



		##############################################

		[name for name in dir(list) if not name.startswith('.')]
		[name for name in dir(turpl) if not name.startswith('.')]


		new_list = list_of_name([:]) # prints entire list 
		new_list = list_of_name([0:2]) # leaves out last name in the list
		# we can use list constructor 
		new_list = list(list_of_name) # less effective 



		import copy 

		class Person:
			def __init__(self, name):
				self.name = name 

			def __repr__(self):
				return self.name 

		Olivia = Person('Olivia')

# new lists of names

		list_of_names = ["Daisy", "Isabel", "Sarah")

		shallow_copy = copy.copy(list_of_names)
		deep_copy = copy.deepcopy(list_of_names)

		slicing = list_of_name[:]
		asterisk = [*list_of_names]
		list_func = list(list_of_name)
		other = list_of_name * 1 
		another = list_of_name + [] 




#exceptions: 

try: 
	f = open('file.txt')

except FileNotFoundError:
	pass


# more than one exception 

try:
	raie AttributeError
except (FileNotFoundError, AttributeError):


#Subclusses for OS error 
except OSError:



ASSERT TEST 

if __debug__:
	if not test:
		raise AssrtionError()


		#python -o ignores assert 



class Specific2(General):
	pass

def raise_gen():
	x = General()
	raise x 

def raise_s1():
	x =Specific1()
	raise x 

def raise_s2():
	x =Specific2()
	raise x 

for fun in (raise_gen, raise_s1, raise_s2):
	try:
		func()
	except General:
		import sys 
		print(f"Caught: {sys.exec_info()}")



#-----------------------------------

except General as e:
	print(f"Caught: {e.__class__}")

#print value as error message 


raise TypeError('Some text here')

E = TypeError('Some text here')
print(E.args)




class CustomError(Exception):
	logfile = 'customerror.log'


	def __init__(self, line, _file):
		self._file = _file 
		self.line  =  line 


		def logerror(self):
			log = open(self.logfile, 'w')
			print(f'CustomError on line {self.line} in file {self._file}', file=log)


	def example_func():
		raise CustomError(50, 'example.file')

	if __name__ == '__main__':
		try:
			example_func()
		except CustomError as e:
			e.logerror




















































