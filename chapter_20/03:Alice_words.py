def count_words(book):
    output = {}

    for word in book:
        if word != 'n':
            output[word] = output.get(word, 0) + 1
    return output

def write_file(filename, write_list):
    '''
        Writes the strings in the list to the file
        erasing all existent content.
    '''
    open(filename, 'w').write('')

    for string in write_list:
            open(filename, 'a').write(string)

def get_words(the_text):
    """
        Return a list of words with al punctuation removed
        with all the letters in lowercase.
    """
    ss = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\"
    ii = "abcdefghijklmnopqrstuvwxyz                                          "
    my_substitutions = the_text.maketrans(ss, ii)

    cleaned_text = the_text.translate(my_substitutions)
    return cleaned_text.split()

def frecuency(some_dict):
    value = 0
    for k in some_dict:
        if value == 0 or some_dict[k] > value:
            value = some_dict[k]
            key = k
    return key, value

def longest_key(some_dict):
    """ Returns the longest key in a dictionary. """
    lenght = 0
    for key in some_dict:
        if len(str(lenght)) == 0 or len(str(lenght)) < len(str(key)):
            lenght = key
    return lenght

def longest_value(some_dict):
    """ Returns the longest value in a dictionary. """
    lenght = 0
    for value in some_dict.values():
        if len(str(lenght)) == 0 or len(str(lenght)) < len(str(value)):
            lenght = value
    return lenght

def dict_to_string(some_dict):
    key_lenght = len(longest_key(some_dict))
    value_lenght = len(str(longest_value(some_dict)))

    some_list = []

    for key in some_dict:
        to_append = f'{str(key).ljust(key_lenght + 1)} {str(some_dict[key]).rjust(value_lenght)}\n'
        some_list.append(to_append)

    SS = ''.join(some_list)
    return SS


filename = '/home/adolfoj/Dev/thinkpython3/src/Chapter_20/resources/Alice_words.txt'
book = '/home/adolfoj/Dev/thinkpython3/src/Chapter_20/resources/Alice.txt'

top = 'Word        Frecuency\n=====================\n'
words = get_words(str(open(book).readlines()))
words.sort()

book_words = count_words(words)

write_file(filename, [top, dict_to_string(book_words)])

print(f'{len(book_words)} lines had been written.')
print(f'{longest_key(book_words).capitalize()} is the longest word.')

print(f'The word "Alice" apears {book_words["alice"]} times.')

print(f'"{frecuency(book_words)[0].capitalize()}" is the most frecuent word;\n'
                       f'It apears {frecuency(book_words)[1]} times.')
