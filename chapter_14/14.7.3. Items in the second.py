from time import time
from items_from_first_list import merge
from get_words_in_book import get_words_in_book
from remove_adjacent_dups import remove_adjacent_dups
from load_words_from_file import load_words_from_file


def items_in_second(first, second):
    return merge(second, first)


bigger_vocab = load_words_from_file("vocab.txt")
all_words = get_words_in_book("AliceInWonderland.txt")


t0 = time()
all_words.sort()
book_words = remove_adjacent_dups(all_words)
unk_words = items_in_second(bigger_vocab, book_words)
t1 = time()

print(f'There are {len(unk_words)} unknown words.'
        f'\nAnd took {t1-t0:.4f} seconds to count them.')
