from time import time
from get_words_in_book import get_words_in_book
from remove_adjacent_dups import remove_adjacent_dups
from load_words_from_file import load_words_from_file

def find_unknowns_merge_pattern(vocab, wds):
    """ Both the vocab and wds must be sorted.  Return a new
        list of words from wds that do not occur in vocab.
    """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            result.extend(wds[yi:])
            return result
        if yi >= len(wds):
            return result
        if vocab[xi] == wds[yi]:  # Good, word exists in vocab
            yi += 1
        elif vocab[xi] < wds[yi]:  # Move past this vocab word,
            xi += 1
        else:                     # Got word that is not in vocab
            result.append(wds[yi])
            yi += 1


bigger_vocab = load_words_from_file("vocab.txt")
all_words = get_words_in_book("AliceInWonderland.txt")

t0 = time()    
all_words.sort()
book_words = remove_adjacent_dups(all_words)
missing_words = find_unknowns_merge_pattern(bigger_vocab, book_words)
t1 = time()

print(f"There are {len(missing_words)} unknown words.")
print(f"That took {t1-t0:.4f} seconds.")
