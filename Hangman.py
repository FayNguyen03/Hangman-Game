#HANGMAN Game
import random
from Word import words
import string
import time

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
       word = random.choice(words)
    return word.upper()

def display_hangman(lives):
    stages = ['''
                --------
                |       |
                |       O
                |      \|/
                |       |
                |       |
                |      / \  
    ''',
    '''
                --------
                |       |
                |       O
                |      \|/
                |       |
                |       |
                |        \  
    ''',
    '''
                --------
                |       |
                |       O
                |      \|/
                |       |
                |       |
                |        
    ''',
    '''
                --------
                |       |
                |       O
                |      \|/
                |       |
                |       
                |         
    ''',
    '''
                --------
                |       |
                |       O
                |      \|/
                |       
                |       
                |         
    ''',
    '''
                --------
                |       |
                |       O
                |      \|
                |       
                |       
                |         
    ''',
    '''
                --------
                |       |
                |       O
                |       |
                |       
                |       
                |         
    ''',
    '''
                --------
                |       |
                |       O
                |      
                |       
                |       
                |         
    ''',
    '''
                --------
                |       |
                |       
                |      
                |       
                |       
                |        
    '''
    ] 
    return stages[lives]  

def hangman():

    word = get_valid_word(words)
    word_letters = set(word) #set of letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 8
    
    #getting user input
    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives,"lives left and you have used these letters:", " ".join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", "".join(word_list),"({})".format(len(word_list)))
        
        user_letter = input("Guess a letter:").upper()
        if user_letter in (alphabet - used_letters):
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives -= 1
                print("Letter is not in word.")
                
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
        
        else:    
            print("Invalid character. Please try again!")
        print(display_hangman(lives))
    
    #When len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print("You died, sorry. The word was " + word +"!")
    else:
        print("You guessed the word " + word + "!")
    
    
hangman()
time.sleep(30)

    
    
