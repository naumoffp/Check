import build
import jar

def main():
    # test_map()
    # test_dict()
    build.rebuild_all()


def test_map():
    """
    Test the KeyMap() class functionality
    get_distance('q', 'm')

    6.324555320336759
    6.324555320336759

    [Done] exited with code=0 in 0.372 seconds
    """
    keys = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    key_map = build.KeyMap(keys)

    print(key_map.get_distance('q', 'm'))

    jar.pickle_entity("cucumber.pkl", key_map)
    new_map = jar.unpickle_entity("cucumber.pkl")

    print(new_map.get_distance('q', 'm'))

    # clean up test file
    jar.remove_file("cucumber.pkl")


def test_dict():
    """
    Test the SpellingDictionary() class functionality
    [Done] exited with code=0 in 1.143 seconds
    """
    spell_dict = build.SpellingDictionary()
    spell_dict.populate_dict("words.txt")

    jar.pickle_entity("dictionary.pkl", spell_dict)
    new_spell_dict = jar.unpickle_entity("dictionary.pkl")
    print(new_spell_dict.words)

    # clean up test file
    jar.remove_file("dictionary.pkl")


if __name__ == "__main__":
    main()
