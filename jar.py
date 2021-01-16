"""

Pickling functions largely derived from:
https://stackoverflow.com/questions/11218477/how-can-i-use-pickle-to-save-a-dict

"""
import pickle
import os

def pickle_entity(filename, entity):
    """ Pickles an entity and saves it to a .pkl file """
    with open(filename, "wb") as handle:
        pickle.dump(entity, handle, protocol=pickle.HIGHEST_PROTOCOL)


def unpickle_entity(filename):
    """ Unpickles an entity from a .pkl file """
    with open(filename, "rb") as handle:
        entity = pickle.load(handle)

    return entity


def remove_file(filename):
    """ Adds an extra layer of saftey to os.remove() by checking if the file exists first """
    # check if the file exists
    if os.path.isfile(filename):
        # delete the file
        os.remove(filename)