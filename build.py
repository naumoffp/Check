from operator import itemgetter

import numpy as np

import jar


class KeyMap(object):
    """ QWERTY Keyboard map class """
    def __init__(self):
        # a list of lists containing n potential rows of characters for a keyboard
        self.keyboard = []

        # this dictionary tells you exactly where each key is located on the keyboard
        # key: character
        # value: tuple of character location (0,0) is first row left
        self.locations = dict()

    def populate(self, characters):
        """Parses strings into rows of individual characters. Modifies the self.keyboard variable.

        Args:
            characters (list): list of strings, each forming an individual row.
        """

        # iterate over each string of characters to populate each row
        for row_index, row in enumerate(characters):
            # add an empty array for each row of characters
            self.keyboard.append([])

            for column_index, key in enumerate(row):
                # normalize the current key to uppercase
                key = key.upper()

                # append key to the current row
                # the current row of characters in the keyboard is defined by row_index
                self.keyboard[row_index].append(key)

                # add location entry for the key
                self.locations[key] = (row_index, column_index)

    def get_distance(self, key_1, key_2):
        """Calculates the euclidean distance between two keys in the self.keyboard variable.

        Args:
            key_1 (char): initial key to calculate distance from.
            key_2 (char): subsequent key to calculate distance to.

        Returns:
            int: distance between key_1 and key_2. if either key does not exist, returns none.
        """

        # find and return the Euclidian Distrance between studenta and studentb
        # from https://www.geeksforgeeks.org/calculate-the-euclidean-distance-using-numpy/
        first_point = np.array(self.locations[key_1])
        second_point = np.array(self.locations[key_2])

        # calculating Euclidean distance
        # using linalg.norm()
        euclidean_distance = np.linalg.norm(first_point - second_point)

        return euclidean_distance

    def get_nearby_keys(self, origin_key, quantity):
        scores = dict()
        # normalize origin key
        origin_key = origin_key.upper()

        # calculate distance score for every nearby key
        for row in self.keyboard:
            for nearby_key in row:
                # ommit the key itself
                if nearby_key != origin_key:
                    # find the proximity of the start key to the current key
                    proximity = self.get_distance(origin_key, nearby_key)
                    # update scores dictionary with the proximity to the current key
                    scores[nearby_key] = proximity

        # extract the n lowest proximities and return the key/value pairs
        # n is defined by the quantity parameter
        # derived from https://www.geeksforgeeks.org/python-smallest-k-values-in-dictionary/
        return dict(sorted(scores.items(), key = itemgetter(1))[:quantity])


class SpellingDictionary(object):
    """ US Dictionary contained in words.txt is from https://github.com/dwyl/english-words/blob/master/words.txt """
    def __init__(self):
        # a regular list would find something in O(n) time complexity
        # a set completes this with a preformance of O(1)
        self.words = set()

    def populate(self, filename):
        """Populates the words set by reading a file of plaintext words seperated by newlines

        Args:
            filename (string): the infile containing the plaintext words
        """
        # using a context manager and iterating over a file line by line,
        # this method is determined to be highly efficient for larger files.
        with open(filename, "r") as infile:
            for line in infile:
                # normalize word to uppercase with no whitespace
                word = line.strip().upper()
                self.words.add(word)

    def is_word(self, word):
        """ Returns true or false depending on if a word is in the dictionary """
        if word in self.words:
            return True

        return False


def rebuild_all(keymap_filename="keymap.pkl", spelldict_filename="en_dict.pkl", words_infile="words.txt"):
    """Deletes old .pkl files and rebuilds current key maps and spelling dictionaries

    Args:
        keymap_filename (str, optional): file to save the keymap to. Defaults to "keymap.pkl".
        spelldict_filename (str, optional): file to save the spelling dictionary to. Defaults to "en_words.pkl".
        words_infile (str, optional): file to build the dictionary out of. Defaults to "words.txt".

    Completion Time: [Done] exited with code=0 in 1.525 seconds
    """

    # clean up old files
    jar.remove_file(keymap_filename)
    jar.remove_file(spelldict_filename)

    # build the keymap
    keys = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    key_map = KeyMap()
    key_map.populate(keys)

    # build the spelling dictionary
    spell_dict = SpellingDictionary()
    spell_dict.populate(words_infile)

    # save the key map and spelling dictionary to a .pkl file
    jar.pickle_entity(keymap_filename, key_map)
    jar.pickle_entity(spelldict_filename, spell_dict)

    print("Files rebuilt!")
