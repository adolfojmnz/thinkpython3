def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    file_content = open(filename, "r").read()
    return file_content.split()

bigger_vocab = load_words_from_file("vocab.txt")
print(f"\n There are {len(bigger_vocab)} words in the vocab, "
        f"staring with:\n {bigger_vocab[:6]}")


