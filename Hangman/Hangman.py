#Sia Ham (1730812)
#420-LCU Computer Programming , Section 3
#S. Hilal , instructor
#Assignment 4


HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
      |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
  |   |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
 /|   |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
 /|\  |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
 /|\  |
 /    |
      |    
=========''', '''

  +---+
  |   |
  o   |
 /|\  |
 / \  |
      |    
=========''']

def allposition(string, sub, listposition=[], offset=0):
   '''find all position of substring in a given string'''
   st_lst = list (string)  
   offset = 0
   listposition = [] #list of all position of subtring in a given string
   while offset< len(st_lst):
      if st_lst.count(sub) ==1:  #condition when there is only one position value
         i = string.find(sub, offset)  
         listposition.append(i)
         return listposition
      elif st_lst.count(sub) > 1: #condition when there are more than one position value
         for offset in range (0, len(st_lst)-1):
            i = string.find(sub, offset)
            listposition.append(i)
            if (-1) in (listposition): #if it returns to -1 (because there is no position), remove -1
                listposition.remove(-1)
            for k in listposition:     # remove the overlapped position value
                if listposition.count(k) >1:
                    listposition.remove(k)
         return listposition
   
def getRandomWord(wordList):
   ''' This function returns a random word from the passed list of words'''
   import random
   wordIndex = random.randint(0, len(wordList) - 1)
   return wordList[wordIndex]

Dict = { } #empty dictionary

animals_txt = open("animals.txt") #read and store each text file
colors_txt = open("colors.txt")
fruit_txt = open("fruits.txt")
shapes_txt = open("shapes.txt")

animals_val = animals_txt.read().split()
colors_val = colors_txt.read().split()
fruit_val = fruit_txt.read().split()
shapes_val = shapes_txt.read().split()

Dict["animals"] = animals_val  #Add code for all 4 files
Dict["colors"] = colors_val
Dict["fruits"] = fruit_val
Dict["shapes"] = shapes_val

x=str(input("Please choose one of the following categories: aniamls, colors, fruits, shapes:")) # ask player to choose a word category.
if (x == 'animals')  or (x == 'colors') or (x == 'fruits') or (x == 'shapes'):   # verify valid input
   random = getRandomWord (Dict[x]) #create a random word from a selected category

   correct_letters = 0
   no_wrong_guesses = 0
   word_dict = {}
   MissedLetters = [] #list for wrong letter guesses
   
   word_guess = "-"*len(random)
   lst_word_guess = list (word_guess) #convert string to list to make to mutable
   wordguess = ''.join (lst_word_guess) #convert list to string
   print ("WordGuess:", wordguess) #display the initial wordguess
   print(HANGMAN [no_wrong_guesses]) #display the initial hangman board
   
   while True:     
      if no_wrong_guesses == 6:   # The player continues to play until the number of allowed guesses is exhausted or the word is revealed 
         print ("game over") 
         break
      elif wordguess == random:
         print ("WordGuess:", wordguess)
         print ("you got the answer!")
         break

      for i in random:
         word_dict [i] = [0]+allposition(random, i) #create a dictionary for the selected random word
         
      guess = str(input("Please guess an alphabet:"))
      if word_dict.get(guess) != None:  #condition for correct guess
         print ("the alphabet you entered is included in the selected random word")
      
      elif word_dict.get(guess) == None: #condition for wrong guess
         MissedLetters.append (guess)
         no_wrong_guesses = len(MissedLetters) 
         print ("the alphabet you entered is NOT included in the selected random word")

     
      for k in random:
         if (guess) ==  (k): #condition for correct guess
            word_dict [k][0] = 1 
            for i in (word_dict [k][1::]): #find the position of an entered number used in the randomly selected word
               lst_word_guess [i] =k
               wordguess = ''.join (lst_word_guess)
 
         if word_dict [k][0] == 1: #count the number of correct guesses
            correct_letters += 1 

      print(HANGMAN [no_wrong_guesses]) #display the hangman board 
      print ("WordGuess:", wordguess) #display wordguess
      print("Following shows a list of wrong letter guesses:", MissedLetters) #display the list of wrong guesses

   
   
else: #verify valid input
   print ("Please choose a valid category")    
         


               
   
               




