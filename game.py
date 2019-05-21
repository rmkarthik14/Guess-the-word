
class game():
    """
    A class to represent the game and store the status

    Attributes
    ----------
    summary : list
        a list to store the status of the game

    """
    summary = []

    def __init__(self,word,status,bad_guess,missed_letters,score):

        """
        Parameters
        ----------
        word : String
            the random word to guess
        status : String
            the status of the game
        bad_guess : int
            the number of bad guesses
        missed_letters : int
            the number of letters blank at the end of each game
        score : int
            the score for the particular game
        """
        self.game = game
        self.word = word
        self.status = status
        self.bad_guess = bad_guess
        self.missed_letters = missed_letters
        self.score = score

    def set_word(self,word):
        """
        Setter for word
        :param word:
        :return:
        """
        self.word = word

    def set_status(self,status):
        """
        setter for status

        :param status:
        :return:
        """
        self.status = status

    def set_bad_guess(self,bad_guess):
        """
        setter for bad_guess
        :param bad_guess:
        :return:
        """
        self.bad_guess = bad_guess

    def set_missed_letters(self,missed_letters):
        """
        setter for missed_letters
        :param missed_letters:
        :return:
        """
        self.missed_letters = missed_letters

    def set_score(self,score):
        """
        setter for score
        :param score:
        :return:
        """
        self.score = score

    def get_word(self):
        """
        getter method for word
        :return:
        """
        return self.word

    def get_status(self):
        """
        getter method for status
        :return:
        """
        return self.status

    def get_bad_guess(self):
        """
        getter method for bad_guess
        :return:
        """
        return self.bad_guess

    def get_missed_letters(self):
        """
        getter method for missed_letters
        :return:
        """
        return self.missed_letters

    def get_score(self):
        """
        getter method for score
        :return:
        """
        return self.score

    def set_summary(self,ob_game):
        game.summary.append(ob_game)

    def get_summary(self):
        return game.summary

    def __repr__(self):
        return str(self.__dict__)