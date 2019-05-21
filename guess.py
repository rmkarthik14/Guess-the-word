from StringDatabase import StringDatabase
from game import game
class guess():
    """
    A class to represent the menu and the game

    Attributes
    ----------
    option : String
        To store the oprion selected by the player
    no_game : int
        to store the number of games played at one instance
    quiz_word : string
        to store the random word

    Methods
    -------
    import_word()
        gets a random word from the StringDatabase class
    start_game()
        starts the game and displays the menu
    word_guess(i_word,i_indices,w_index)
        method that executes when the user selects guess option and guesses the word
    tell(i_word,i_indices,w_index)
        method that when the user gives up and the method displays the word
    quit(i_word,i_indices,w_index)
        the user quits the game
    lett(i_word,i_indices,w_index)
        the user tries to guess the letter and the method checks the correctness of the letter
    calc_score(i_word,i_indices)
        calculates the score
    print_summary(s_list)
        prints the summary of the game at the end
    """
    option = ""
    indices = [0, 0, 0, 0]
    w_index = {}
    quiz_word = ""
    no_letter_req = 0
    no_wrong_guess = 0
    no_game = 0
    summary = []

    def import_word(self):
        """
        gets a random word from the StringDatabase class
        :return:
        """

        data = StringDatabase()
        guess.quiz_word = data.getWord()
        #print(guess.quiz_word)

    def start_game(self):
        """
        starts the game and displays the menu
        :return:
        """
        print("\n**The Great Guessing Game**")
        print("Current Guess: ", end="")
        for i in guess.indices:
                if i == 0:
                    print("-", end="")
                else:
                    print(i, end="")
        print("\ng= guess, t= tell me, l for a letter, and q to quit")
        option = input()
        if option.lower() == 'g':
            guess.word_guess(self,guess.quiz_word,guess.indices,guess.w_index)
        elif option.lower() == 't':
            guess.tell(self,guess.quiz_word,guess.indices,guess.w_index)
        elif option.lower() == 'l':
            guess.no_letter_req += 1
            guess.lett(self,guess.quiz_word,guess.indices,guess.w_index)
        elif option.lower() == "q":
            guess.quit(self,guess.quiz_word,guess.indices,guess.w_index)
        else:
            print("Wrong option. Enter correct option from menu\n")
            guess.start_game(self)

    def word_guess(self,i_word,i_indices,w_index):
        """
        method that executes when the user selects guess option and guesses the word
        :param i_word: the word to guess
        :param i_indices: the uncovered letters
        :param w_index: the index of the uncovered letters
        :return:
        """
        g_word = input("Enter the guess: ")
        if g_word.lower() == i_word:
            print("Correct Guess \n")
            l_score = guess.calc_score(self,i_word,i_indices)
            t_score = l_score[1]
            missed_letters = 4 - len(w_index)
            t_game = game(i_word, "success", guess.no_wrong_guess, missed_letters, t_score)
            guess.summary.append(t_game)
            guess.cl_att(self)
            guess.import_word(self)
            guess.no_game += 1
            if guess.no_game <= 100:
                guess.start_game(self)
            else:
                print("Game ended...")
                guess.print_summary(self,guess.summary)
        else:
            print("Wrong Guess... Try Again...\n")
            guess.no_wrong_guess +=1
            guess.start_game(self)

    def tell(self,i_word,i_indices,w_index):
        """
        method that when the user gives up and the method displays the word
        :param i_word: the wor to guess
        :param i_indices: the index of the uncovered letters
        :param w_index: the uncovered letters
        :return:
        """
        print("Word is ", i_word,"\n")
        l_score = guess.calc_score(self, i_word, i_indices)
        g_score = l_score[0]
        t_score = 0
        t_score = t_score-g_score
        #print(t_score)
        missed_letters = 4 - len(w_index)
        t_game = game(i_word,"gave up",guess.no_wrong_guess,missed_letters,t_score)
        guess.summary.append(t_game)
        guess.cl_att(self)
        guess.import_word(self)
        guess.no_game += 1
        if guess.no_game <= 100:
            guess.start_game(self)
        else:
            print("Game ended")
            guess.print_summary(self,guess.summary)

    def quit(self,i_word,i_indices,w_index):
        """
        the user quits the game
        :param i_word: the word to guess
        :param i_indices: the index of the uncovered letters
        :param w_index: the uncovered letters
        :return:
        """
        quit_choice = input("Are you sure?\nEnter 'y' for 'yes' and 'n' for 'no': \n")
        if quit_choice.lower() != "y" and quit_choice.lower() != "n":
            print("\nWrong option... Enter 'y' or 'n'")
            guess.quit(self,i_word,i_indices,w_index)
        elif quit_choice.lower() == "y":
            if guess.no_wrong_guess > 0 or guess.no_letter_req > 0:
                print("Word is ", i_word, "\n")
                l_score = guess.calc_score(self, i_word, i_indices)
                g_score = l_score[0]
                t_score = 0
                t_score = t_score - g_score
                missed_letters = 4 - len(w_index)
                t_game = game(i_word, "gave up", guess.no_wrong_guess, missed_letters, t_score)
                guess.summary.append(t_game)
            print("Thanks for playing!!!")
            guess.print_summary(self,guess.summary)
        elif quit_choice.lower() == "n":
            print("Continue to play the game...")
            guess.start_game(self)

    def lett(self, i_word,i_indices,w_index):
        """
        the user tries to guess the letter and the method checks the correctness of the letter
        :param i_word: the word to guess
        :param i_indices: the index of the uncovered letters
        :param w_index:  the uncovered letters
        :return:
        """
        ip_letter = input("Enter the letter:")
        ctr = 0
        ct_fg = 0
        for i in i_word:
            if i == ip_letter.lower():
                ct_fg += 1
                guess.indices[ctr] = i
                guess.w_index[ctr] = i
            ctr += 1
        print("you found ",len(guess.w_index)," letters")
        #print(guess.indices)
        #print(guess.w_index)
        if ct_fg == 0:
            print("Worng letter... Please try again")
            guess.start_game(self)
        elif len(guess.w_index)== 4:
            print("\nCongrats... Correct answer!!!\nThe word is ",i_word)
            l_score = guess.calc_score(self,i_word,i_indices)
            t_score = l_score[1]
            missed_letters = 4 - len(w_index)
            t_game = game(i_word, "success", guess.no_wrong_guess, missed_letters, t_score)
            guess.summary.append(t_game)
            guess.cl_att(self)
            guess.import_word(self)
            guess.no_game += 1
            if guess.no_game <= 100:
                guess.start_game(self)
            else:
                print("Game ended...")
                guess.print_summary(self,guess.summary)
        else:
            guess.start_game(self)

    def cl_att(self):
        guess.option = ""
        guess.indices = [0, 0, 0, 0]
        guess.w_index = {}
        guess.quiz_word = ""
        guess.no_letter_req = 0
        guess.no_wrong_guess = 0
        guess.game_no = 0

    def calc_score(self,i_word,i_indices):
        """
        Calculates the score
        :param i_word: the word to guess
        :param i_indices: the index of the uncovered letters
        :return:
        """
        uncovered_index = []
        uncovered_letters = []
        uncovered_score = 0
        frequency_dic = {"a": 8.17, "b": 1.49, "c": 2.78, "d": 4.25, "e": 12.70, "f": 2.23, "g": 2.02, "h": 6.09,
                         "i": 6.97, "j": 0.15, "k": 0.77, "l": 4.03, "m": 2.41,
                         "n": 6.75, "o": 7.51, "p": 1.93, "q": 0.10, "r": 5.99, "s": 6.33, "t": 9.06, "u": 2.76,
                         "v": 0.98, "w": 2.36, "x": 0.15, "y": 1.97, "z": 0.07, }
        for index, elements in enumerate(i_indices):
            if elements == 0:
                uncovered_index.append(index)
        for i in uncovered_index:
            uncovered_letters.append(i_word[i])
        for s in uncovered_letters:
            uncovered_score = frequency_dic[s] + uncovered_score
        if guess.no_letter_req == 0:
            r_uncovered_score = uncovered_score
        else:
            r_uncovered_score = uncovered_score / guess.no_letter_req
        prcnt = guess.no_wrong_guess*10
        g_uncovered_score = r_uncovered_score-((prcnt*r_uncovered_score)/(100))
        l_score = [uncovered_score,g_uncovered_score]
        #print("Uncovered score: ", uncovered_score, r_uncovered_score,g_uncovered_score)
        return l_score

    def print_summary(self,s_list):
        """
        Prints the summary of the game at the end
        :param s_list: the list of summaries
        :return:
        """
        print("\n|Game|\t|Word|\t|status|\t|Bad Guesses|\t|Missed Letters|\t|Score|")
        game_no =1
        final_score =0
        for obs in s_list:
            print(game_no,"\t",obs.get_word(),"\t",obs.get_status(),"\t",obs.get_bad_guess(),"\t\t\t",obs.get_missed_letters(),
                  "\t\t", format(obs.get_score(),'.2f'))
            final_score = obs.get_score()+final_score
            game_no += 1
        print("Final Score: ", format(final_score,'.2f'))

def main():
    play_guess = guess()
    play_guess.import_word()
    play_guess.start_game()

if __name__ == "__main__":
    main()