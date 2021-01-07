#Sia Ham (1730812)
#420-LCU Computer Programming , Section 3
#Monday , September 17th
#S. Hilal , instructor
#Assignment 1

#Exercise 1


high = 100    # Define the upper limit of the range.
low = 0       # Define the lower limit of the range.
guess = int((high + low)/2)     #start in the middle of the possible range using Bisection search

print ("Please think of a number(integer) between 1 and 100.")
while True:
    print("Is your secret number " + str(guess)+" ?")
    comment = input("Enter 'h' if my guess is too high, 'l' if too low, or 'c' if I am correct:")
    if comment == "h":
        high = guess
        guess = int((guess + low)/2)     #If the guess is too high, use the lower half by choosing a new guess to be the midpoint of the new range    
    elif comment == "l":
        low = guess
        guess = int((guess + high) / 2)  #If the guess is too low, use the upper half by choosing a new guess to be the midpoint of the new range      
    elif comment == "c":
        print ( "Game over, your secret number was:" + str(guess))
        break
       
