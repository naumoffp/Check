import build
import jar
import colorama
import builtins
import ui
import sys

KEYMAP = None
DICTIONARY = None


def main():
    # initialize color display library and custom printing function
    colorama.init()
    builtins.print = ui.delayed_print

    # build.rebuild_all()

    # initialize spell checking instances from files
    global KEYMAP
    global DICTIONARY

    KEYMAP = jar.unpickle_entity("keymap.pkl")
    DICTIONARY = jar.unpickle_entity("en_dict.pkl")

    display_main_menu()


def suggest_correction(word):
    # normalize word
    word = word.upper()

    # defines the scope of keys that the suggestion algorithm will scan
    # example: reach = 4 will scan up to 4 keys away from the origin key
    reach = 8

    # this dictionary contains all proximity based word suggestions
    # key: suggested word
    # value: proximity score
    suggestions = dict()

    # evaluate all potential letters and build a confidence score
    for key_index, origin_key in enumerate(word):
        # find all the nearby keys around the enumerated origin key
        nearby_keys = KEYMAP.get_nearby_keys(origin_key, reach)

        # add substitutions for every character in the word
        for nearby_key, proximity in nearby_keys.items():
            # map bounds around the origin_key so that the nearby key can replace it to formulate a word
            lower_bound = key_index
            upper_bound = key_index + 1

            # optimization: fastest method to splice a character with a string
            # tested on 'hallo' with a reach of 1: YALLO, HQLLO, HAOLO, HALOO, HALLI
            first_half = word[:lower_bound]
            second_half = word[upper_bound:]

            modified_word = first_half + nearby_key + second_half
            if DICTIONARY.is_word(modified_word):
                # add valid word to the suggestions dictionary tagged with a proximity value
                suggestions[modified_word] = proximity


    return suggestions


def spell_check_this():
    ui.clr()

    spell_check_menu = ui.Menu("Spell Check This™")
    spell_check_menu.display(False)

    print("\n")
    print("Word To Spell Check >> ")
    word = input()

    # normalize the input
    word = word.upper()

    if not DICTIONARY.is_word(word):
        print("\n")

        # spell check the word
        suggestions = suggest_correction(word)

        if ui.prompt("Verbose Logging?"):
            print("\n")
            print("DICTIONARY FORMAT (Suggested Word: Proximity Score):\n", "red")
            print(suggestions)
            print("\n\n")

        # print the suggestion with the lowest proximity score
        print("Suggestion: ")
        if suggestions:
            print(min(suggestions, key=suggestions.get), "green")
        else:
            print("None, word is garbled.")

        print("\n")

    else:
        print("\n")
        print("Input is a valid word!\n", "green")


def about():
    ui.clr()
    print("Spell Check This™\n")
    print("Created by Peter Naumoff\n", "green")


def display_main_menu():
    """ displays the main menu """

    main_menu = ui.Menu("Spell Check This™")

    main_menu.add("Spell Check a Word", spell_check_this)
    main_menu.add("About", about)
    main_menu.add("Exit", sys.exit, 0)

    main_menu.display()

if __name__ == "__main__":
    main()
