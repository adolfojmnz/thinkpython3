from time import time
from binary_search import search_binary
from find_unknown_words import find_unknown_words
from load_words_in_file import load_words_from_file
from get_words_in_book import get_words_in_book


bigger_vocab = load_words_from_file("vocab.txt")
book_words = get_words_in_book("AliceInWonderland.txt")

#t0 = time()
#missing_words = find_unknown_words(bigger_vocab, book_words)
#t1 = time()
#print("There are {0} unknown words.".format(len(missing_words)))
#print("That took {0:.4f} seconds.".format(t1-t0))
 
search_binary(bigger_vocab, "magic")
