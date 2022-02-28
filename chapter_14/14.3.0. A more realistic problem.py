from linear_search import search_linear 


def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if (search_linear(vocab, w) < 0):
            result.append(w)
    return result


vocab = ["apple", "boy", "dog", "down",
         "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()
print(find_unknown_words(vocab, book_words) == ["from", "to"])
print(find_unknown_words([], book_words) == book_words)
print(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])
