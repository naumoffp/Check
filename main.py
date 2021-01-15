import build
import jar

def main():
    keys = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    key_map = build.KeyMap(keys)
    print(key_map.get_distance('q', 'm'))

    jar.pickle_entity("cucumber", key_map)
    new_map = jar.unpickle_entity("cucumber")

    print(new_map.get_distance('q', 'm'))

if __name__ == "__main__":
    main()
