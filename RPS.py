import random

def check(user,computer):
	if user == 1 and computer==2:
		return 1
	elif user == 1 and computer==3:
		return 0
	elif user == 2 and computer==1:
		return 0
	elif user == 2 and computer==3:
		return 1
	elif user == 3 and computer==1:
		return 1
	elif user == 3 and computer==2:
		return 0

def show():
	user_win=0
	computer_win=0
	for i in range(0,3):
		while(True):
			user= int(input("\t\t\t\t\t\t\tEnter your Choice:\t\t\t\t\t\t\t\n -> Input 1 for Rock\n -> Input 2 for Paper\n -> Input 3 for Scissors\n "))
			if user<1 and user>3:
				print("Enter Valid Input\n")
			else:
				break
		if user==1:
			print("You Entered Rock")			
		elif user==2:
			print("You Entered Paper")			
		elif user ==3:
			print("You Entered Scissors")
			

		print("\n")

		while(True):
			computer= random.randrange(1,4)
			if computer==1:
				print("Computer Entered Rock")
				break
			elif computer==2:
				print("Computer Entered Paper")
				break
			elif computer ==3:
				print("Computer Entered Scissors")
				break
		print("\n")

		res= check(user,computer)
		if res==0:
			user_win+=1
		elif res==1:
			computer_win+=1

		print("Round- {} complete".format(i+1),end="\n")
	if user_win > computer_win:
		print("Congrats!! You Won")
	elif user_win < computer_win:
		print("You Lost!! Better Luck Next Time")
	else:
		print("Its a Tie!!")


show()


