########################################
# Name:
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr):
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.
    #milestone #0
    gw = WordleGWindow()
    word='HELLO'
    for i in range(len(word)):
        gw.set_square_letter(0, i, word[i])


    #milestone #1
    def enter_action():
        word =''
        if word in ENGLISH_WORDS: 
            gw.show_message("hooray")
        else: 
            gw.show_message("womp womp")

    gw.add_enter_listener(enter_action)






# Startup boilerplate
if __name__ == "__main__":
    wordle()
