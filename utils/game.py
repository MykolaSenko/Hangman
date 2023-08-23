import sys     # Import sys for sys.exit() when the game is over
import os      # Import os to check OS when using self.clear() method 
from wonderwords import RandomWord    # Import wonderwords for chosing random English word

class Hangman():         # Creating Hangman class
    def __init__(self):   # Defining method "Constructer" to esteblish all needed attributes
        r = RandomWord()     # Create an instance of RandomWord
        self.word_to_find = r.word()    # Esteblishing attribute with generated random word
        # Esteblishing other attributes
        self.correctly_guessed_letters = ['_'] * len(self.word_to_find)
        self.wrongly_guessed_letters = []
        self.lives = 10
        self.turn_count = 0
        self.error_count = 0

    def play(self):         # defining 'play' method which check the input letter, change counters, check if a player guessed the right letter
        players_letter = input('Please enter your letter here: ').lower()      # input the letter
        self.turn_count += 1
        while not players_letter.isalpha() or len(players_letter) > 1:            # check if input symbol is alphabetic and if a player input only 1 symbol
            players_letter = input('You have entered an invalid character. Please enter a single letter: ').lower()

        if players_letter in self.word_to_find:              # checking if a player's letter is in the word which has to be found. If yes, it writes the letter into a priper space of the list correctly_guessed_letters
            for h in range(len(self.word_to_find)):
                if players_letter == self.word_to_find[h]:
                    self.correctly_guessed_letters[h] = players_letter
        else:                                                 # if no, submit the letter to the list of wrongly guessed letters
            self.wrongly_guessed_letters.append(players_letter)
            self.error_count += 1
            self.lives -= 1
        self.start_game()                             # initialising start game method

    def start_game(self):                    # defining start game method
        self.clear()                          # cleaning a screen from former loop
        # printing messages
        print('Correctly guessed letters:', " ".join(self.correctly_guessed_letters))
        print('Wrong letters:', " ".join(self.wrongly_guessed_letters))
        print('Lives:', self.lives)
        print('Error count:', self.error_count)
        print('Turn count:', self.turn_count)
        while True:                     # checking if the game is over. If yes, call for 'game over' or 'well played' method. If no, call for 'play' method
            if '_' not in self.correctly_guessed_letters:
                print('Well done! You won!')
                self.well_played()
            elif self.lives == 0:
                print('You have no more lives!')
                self.game_over()
            else:
                self.play()

    def game_over(self):                    # defining 'game over' method
        print('Game over!')
        print(f'The word was: {self.word_to_find}')
        sys.exit()

    def well_played(self):                 # defining 'well played' method
        print(f'You found the word: {"".join(self.correctly_guessed_letters)} in {self.turn_count} turns with {self.error_count} errors!')
        sys.exit()

    def clear(self):                      # defining 'clear' method which erase all previous information from the screen
        if os.name == 'nt':     # for windows
            _ = os.system('cls')
        else:                   # for mac and linux(here, os.name is 'posix')
            _ = os.system('clear')

hangman = Hangman()
hangman.start_game()