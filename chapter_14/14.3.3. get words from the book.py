import time
from text_to_words import text_to_words
from load_words_in_file import load_words_from_file
from find_unknown_words import find_unknown_words

def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    return text_to_words(open(filename).read())


book_words = get_words_in_book("AliceInWonderland.txt")

t0 = time.process_time()
missing_words = find_unknown_words(
    load_words_from_file("vocab.txt"), book_words)
t1 = time.process_time()


print(f"There are {len(book_words)} words in the book")
#            f"the firsts 100 are:\n{book_words[:100]}")
print(f"There are {len(missing_words)} unknown words.")
print(f"And took {t1-t0:4f} seconds to count them.")