import numpy as np


class KeyMap(object):
    """ QWERTY Keyboard map class """
    def __init__(self, characters):
        # this list of list contains three rows of potential characters for a keyboard
        self.keyboard = [[], [], []]

        # this dictionary tells you exactly where each key is located on the keyboard
        # key: character
        # value: tuple of character location (0,0) is first row left
        self.locations = dict()

        # populate the above variables
        self.populate_map(characters)

    def populate_map(self, characters):
        """Parses strings into rows of individual characters. Modifies the self.keyboard variable.

        Args:
            characters (list): list of strings, each forming an individual row.
        """
        # iterate over each string of characters to populate each row
        for row_index, row in enumerate(characters):
            for column_index, key in enumerate(row):
                # normalize the current key to uppercase and append it to the current row
                # the current row of characters in the keyboard is defined by row_index
                self.keyboard[row_index].append(key.upper())

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


class SpellDict(object):
    """ US Dictionary """
    def __init__(self):
        pass
