 guess = 0
 luckyNumber = (int) Math.random() * 10;

while guess != luckyNumber:
    guess = int(input("Enter a number: "))
	
			
if(guess > luckyNumber):
    print("Too high, try again") 

else if(guess < luckyNumber):
    print("Too low, try again")
			
else if(guess == luckyNumber):
    print("you won")
			