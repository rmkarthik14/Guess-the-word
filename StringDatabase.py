import random

class StringDatabase():
    """
    A class to represent the string database

    Attributes
    ----------
    word_list : list
        a list to store the 4 letter words

    Methods
    -------
    getWord()
        returns a random word from the document

    """
    word_list = []

    def getWord(self):
        """
        returns a random word from the document

        Parameters: none
        """

        four_letter_file = open("four_letters.txt")
        lines = four_letter_file.readlines()
        for line in lines:
            ln = line.split()
            StringDatabase.word_list.append(ln)

        ra_list = random.choice(StringDatabase.word_list)
        word = random.choice(ra_list)
        #print(word)
        four_letter_file.close()
        return word