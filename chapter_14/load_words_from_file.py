def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    file_content = open(filename, "r").read()
    return file_content.split()
