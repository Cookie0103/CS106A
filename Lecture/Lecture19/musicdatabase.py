"""
File: musicdatabase.py
---------------------
This program provides an example of parsing strings from a file
using the "find" function to look for specific character delimiters
in strings to break them up into components.
"""


INPUTFILE = 'data/music.txt'    # File containing music library data
NUM_COMPONENTS = 4              # Number of components on each line of input file


def parse_line(line):
    """
    Parses one line from input file into its various components.  Returns a
    list containing the components in the same order as they are listed in file.
    """
    list = []
    end = 0
    for i in range(NUM_COMPONENTS):
        start = line.find('[', end) + 1     # Find starting position of component
        end = line.find(']', start)         # Find one past ending position of component
        list.append(line[start:end])        # Add substring representing the component to list
    return list


def load_music_data(filename):
    """
    Loads all of the data from the given filename into a dictionary.  The keys in
    the dictionary are song names.  The value is a dictionary containing other
    attributes of the song, such as artist, album, and genre.
    """
    music_data = {}
    with open(filename) as file:
        next(file)                  # Skip header line
        for line in file:
            line = line.strip()
            parts = parse_line(line)
            key = parts[0]          # Key is song name
            value = {               # Value is dictionary of data about song
                'Artist': parts[1],
                'Album': parts[2],
                'Genre': parts[3]
            }
            music_data[key] = value

    return music_data


def list_songs(music_data):
    """
    Lists all the song names in the music data.
    """
    print("List of all songs:")
    for key in music_data:
        print(key)


def main():
    data = load_music_data(INPUTFILE)
    while True:
        song = input('Enter a song ("list" to see all songs): ')
        if song == '':
            break
        elif song == 'list':
            list_songs(data)
        elif song not in data.keys():
            print(song + ' is not in the music data.')
        else:
            info = data[song]
            print(info)


if __name__ == '__main__':
    main()
