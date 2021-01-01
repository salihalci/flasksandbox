


def whileLoopExample():
	count=0
	movies=["Movie1","Movie2"]
	while count<len(movies):
		print(movies[count])
		count=count+1


def forLoopExample():
	names=["name1","name2","name3"]
	for x in names:
		print(x)
def nestedListExampe():
	movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese","Terry Gilliam", "Eric Idle", "Terry Jones"]]]
	print(movies)

	print("------------")
	for item in movies:
		print(item)
	print("------------")

	print(movies[4][1][1])


def nestedListExtendedExample(movies):
#Test data for input
#	movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese","Terry Gilliam", "Eric Idle", "Terry Jones"]]]
	
	for item in movies:
		if isinstance(item, list): # if nested item is a list than loop again
			nestedListExtendedExample(item)
		else:
			print(item)		
def printList(list):
	for item in list:
		print(item)	

def functionReturnExample()->str:
	return ("Test string")

def ifElseExample(input):
	if input=="test" :
		print("input is test")
	else:
		pass

def isInstanceExample(input):
		#isInstance is a BIF(built in function)
	if isinstance(input,list):
		print("Input is a list")
	else:
		print("Input is not list")


def forLoopExample1():
	for x in [1,"3","-"]:
		print(x)

if __name__=='__main__':

	#print("Hello")
	#print()
	#whileLoopExample();
	#forLoopExample()
	#print(functionReturnExample())
	#
	# nestedListExampe()
# 	ifElseExample("test")
#	ifElseExample("1")

#	myList = ["Item1","Item2"]
#	isInstanceExample(myList)

#	movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese","Terry Gilliam", "Eric Idle", "Terry Jones"]]]
#	nestedListExtendedExample(movies)

	forLoopExample1()
