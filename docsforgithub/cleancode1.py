# import sys

# def hello():
# 	return 1 + dict()

# try:
# 	hello()
# except Exception:
# 	for _ in sys.exec_info():
# 		print(_)


# #####################################

# import traceback 

# def divide_by_zero(x):
# 	return x / 0

# try: 
# 	divide_by_zero(5)
# except Exception:
# 	# use traceback print module 
# 	traceback.print_exc(file=open('traceback.file', 'w'))
# print('not in file')



# how to design more smartly with Exceptions 
#---------------------control flow 
#- catch error of func1 try to add  tuple and dict 
#- custom Exception handler - & print its inner try block 


# def func2():
# 	return tuple() + dict()

# def func1():
# 	try:
# 		func2()
# 	except TypeError:
# 		print(" Inner try block")
# # wrap func one in a very similar func handler 

# try: 
# 	func1()
# except TypeError:
# 	print("Outer try block")


# to know where you will go you need to know where you've been 
# where exceptions are handled
# its a functional flow  that exception syntax 


# try:
# 	try:
# 		raise AttributeError
# 	finally:
# 		print("Lowercase")
# finally:
# 	print("UPPERCASE ONLYFOLLOWED BY OUR EXCEPTION")


##############################################
# OPERATOR OVERLOADING - intercept built in operations ina class method 


# class User:
# 	def __init__(self, name):
# 		self.name = name 

# # create instance of the class object lp 

# lp = User('lp')

# print(lp)

# have a wrapper method to return the info of user we need 


class User:
	def __init__(self, name):
		self.username =  name 

	# Wrapper method which returns self 

	def __repr__(self):
		return (f"Instance {self.username} of class user")

	def __str__(self):
		return  (f"{self.username} user-friendly. Debug info in __repr__")


lp = User('lp')

print(lp)
print(lp.__str__())
print(lp)



# using both reper and str (__str__)
# python first look for dander string definition  if its not defined 
#then return value of wrapper is used (__str__)

# 




















