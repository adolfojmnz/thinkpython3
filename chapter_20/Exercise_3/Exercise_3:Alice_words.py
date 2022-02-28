from longest_in_dict import longest_key
from write_file import write_file
from count_words import count_words
from extract_words import get_words
from the_most_frecuent import frecuency
from dict_to_string import dict_to_string


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