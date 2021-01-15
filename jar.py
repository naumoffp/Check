"""

Pickling functions largely derived from:
https://stackoverflow.com/questions/11218477/how-can-i-use-pickle-to-save-a-dict

"""
import pickle

def pickle_entity(filename, entity):
    """ Pickles an entity and saves it to a .pkl file """
    with open(filename + ".pkl", "wb") as handle:
        pickle.dump(entity, handle, protocol=pickle.HIGHEST_PROTOCOL)


def unpickle_entity(filename):
    """ Unpickles an entity from a .pkl file """
    with open(filename + ".pkl", "rb") as handle:
        entity = pickle.load(handle)

    return entity