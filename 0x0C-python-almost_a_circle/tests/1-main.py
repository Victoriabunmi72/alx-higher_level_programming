#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file('my
        _first_file.txt', 'This School is so cool!\n')
print(nb_characters)
