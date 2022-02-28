from text_to_words import text_to_words


def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    return text_to_words(open(filename).read())
