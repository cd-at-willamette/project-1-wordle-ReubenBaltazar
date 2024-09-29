########################################
# Name: Reuben Baltazar
# Collaborators (if any): N
# GenAI Transcript (if any): N
# Estimated time spent (hr): 13
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    gw = WordleGWindow()

    # milestone 3: picks a random 5-letter word
    five_letter_words = [word for word in ENGLISH_WORDS if len(word) == 5]
    answer = random.choice(five_letter_words).lower()  
    print(answer)

    # milestone 1: check validity
    def enter_action():
        current_row = gw.get_current_row()
        guess_str = ""
        for i in range(5):
            guess_str += gw.get_square_letter(gw.get_current_row(), i)
        guess_str = guess_str.lower()

        if guess_str in five_letter_words:  
            gw.show_message("you're not dumb!")
            color_row(gw.get_current_row(), guess_str, answer)
        else:
            gw.show_message("not a word bozo")
            
        #milestone 4: change rows
        if guess_str in five_letter_words and guess_str == answer: 
            gw.show_message("you are intelligent.")
            gw.set_current_row(N_ROWS)
        else: 
            if current_row + 1 < N_ROWS:
                gw.set_current_row(current_row + 1)
            else:
                # If the user has reached the last row and failed
                gw.show_message(f"the correct word was {answer}.")
        # milestone 2/5: colors
    def color_row(row, guess, answer):   
        used_letters = list(answer)
        
        # correct letter and position loop
        for i in range(5): 
            if guess[i] == answer[i]:
                gw.set_square_color(row, i, CORRECT_COLOR)
                used_letters[i] = None  
                gw.set_key_color(guess[i], CORRECT_COLOR)

        # correct letter but wrong position loop
        for i in range(5): 
            if gw.get_square_color(row, i) != CORRECT_COLOR and guess[i] in used_letters:
                gw.set_square_color(row, i, PRESENT_COLOR)
                used_letters[used_letters.index(guess[i])] = None
                gw.set_key_color(guess[i], PRESENT_COLOR)


        # incorrect letter loop 
        for i in range(5): 
            if gw.get_square_color(row, i) not in [CORRECT_COLOR, PRESENT_COLOR]:
                gw.set_square_color(row, i, MISSING_COLOR)
                gw.set_key_color(guess[i], MISSING_COLOR)

    gw.add_enter_listener(enter_action)







# Startup boilerplate
if __name__ == "__main__":
    wordle()
