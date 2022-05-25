#Wordle Game
#Ideas:
#   5, 6, and 7 letter wordle
#   Insane mode that does not tell you if the letter is in the right place
#   Players can add new words to word bank

#For now I have used a text document with 650 words to test the program.

import random, string

class Wordle():
    def __init__(self):
        self.currentword = None
        self.wordbankarray = []
        self.currentlettersguessed = []
        self.currentlettersinrightplace = []
        self.currentlettersinrightplaceindex = []
        self.currentlettersinword = []
    
    def getword(self): #Grabs the first word after shuffling the words and changes current word to the selected word
        random.shuffle(self.wordbankarray)
        self.currentword = self.wordbankarray[0]

    def gamestart(self): #Grabs from the word bank all the words and lowercases them to get them ready for grabbing the word from the function above
        words = open('C:\\Users\\kaors\\Documents\\Myprograms\\Wordle Game\\words.txt','r')
        for line in words:
            for word in line.split():
                self.wordbankarray.append(word.lower())

    def displayguesses(self):
        for index in range(len(self.currentlettersguessed)):
            if index == 0:
                print(self.currentlettersguessed[index],end='')
                continue
            print(self.currentlettersguessed[index],end='') 
            if (index+1) % 5 == 0:
                print(f'\n')

        
    def playerguess(self):
        while True:
            playerinput = input('Please guess a 5 letter word ')

            if len(playerinput) == 5: #If correct input is provided -> append to current letters guessed to win check and change current guess
                if playerinput in self.wordbankarray:
                    for letters in range(len(playerinput)):
                        self.currentlettersguessed.append(playerinput[letters])
                    if playerinput.lower() == self.currentword:
                        return True #This will be the deciding factor to check if we won the game or not. Once it returns positive then we will end the game in the while loop
                    else:
                        return False #Since it returns false we will loop through the main function again
                else:
                    print('Word is not in my word bank! Please try a different word!')
                    continue

            if len(playerinput) != 5: #If incorrect input is provided
                print('Word is not 5 letters. Please try again')
                continue

    def wincheck(self):
        #Check letter index of all guesses if it is in the right place
        for index in range(0,5):
            for letter in range(index,len(self.currentlettersguessed),5):
                if self.currentlettersguessed[letter] == self.currentword[index]:
                    if self.currentlettersguessed[letter] in self.currentlettersinrightplace:
                        continue
                    else:
                        self.currentlettersinrightplace.append(self.currentlettersguessed[letter])
                        self.currentlettersinrightplaceindex.append(index+1)
        #If it is in the right place then it will be in the word so we will add these first
        for letter in range(0,len(self.currentlettersinrightplace)):
            if self.currentlettersinrightplace[letter] in self.currentlettersinword:
                continue
            else:
                self.currentlettersinword.append(self.currentlettersinrightplace[letter])
        #After adding the current letters we have in the right place then we will add the remaining letters that are not in the right place while making sure we don't repeat these letters
        for letter in range(0,len(self.currentlettersguessed)):
            if self.currentlettersguessed[letter] in self.currentword:
                if self.currentlettersguessed[letter] in self.currentlettersinword:
                    continue
                else:
                    self.currentlettersinword.append(self.currentlettersguessed[letter])
        if self.currentlettersinword:
            print(f'The letters {*self.currentlettersinword,} are in the word!')
            if self.currentlettersinrightplace:
                print(f'The letters {self.currentlettersinrightplace} are in the right place of {self.currentlettersinrightplaceindex} from place 1-5!')
            else:
                print('None of the letters are in the right place!')
        else:
            print('None of the letters are in the word!')
        #Return unique letters guessed so far and pending letters in the alphabet sorted
        lettersguessed = set(self.currentlettersguessed)
        alphabetlist = string.ascii_lowercase
        lettersmissing = list(set(lettersguessed)^set(alphabetlist))
        lettersmissing.sort()
        print(f'Unique letters guessed so far {lettersguessed}')
        print(f'Unique letters that have not been used {lettersmissing}')
        #Neat format that shows which place of the word you have gotten so far
        attemptedword = ''
        attemptedindex = 0
        for letter in range(1,6):
            if letter in self.currentlettersinrightplaceindex:
                attemptedword += self.currentlettersinrightplace[attemptedindex]
                attemptedindex += 1
            else:
                attemptedword += 'x'
        print(f'Attempted word so far is: {attemptedword}')

def replay(): #Check to see if the player wants to play again
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')        


print('Welcome to Wordle!')
wordlegame = Wordle()
wordlegame.gamestart() #Inititates array of letters from text document

while True:
    # Resets the current word and arrays
    wordlegame.getword()
    wordlegame.currentlettersguessed = []
    wordlegame.currentlettersinword = []
    wordlegame.currentlettersinrightplace = []
    wordlegame.currentlettersinrightplaceindex = []

    #Check to see if the player wants to play

    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        break


    while game_on:
        if len(wordlegame.currentlettersguessed) >= 30: #Ends game if the player has guessed more than 5 words
            print(f'Game Over! You have ran out of attempts! The correct word was {wordlegame.currentword}')
            break
        if wordlegame.playerguess() == True: #Ends game if the player guesses the word properly
            print(f'Congratulations the word was {wordlegame.currentword}!')
            break
        wordlegame.displayguesses()
        wordlegame.wincheck()

    if not replay():
        break
