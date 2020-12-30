
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

def functionReturnExample()->str:
	return ("Test string")




if __name__=='__main__':
	#print("Hello")
	#print()
	#whileLoopExample();
	#forLoopExample()
	#print(functionReturnExample())
	nestedListExampe()