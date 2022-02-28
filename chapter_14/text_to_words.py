def text_to_words(the_text):
    """
        Return a list of words with al punctuation removed
        with all the letters in lowercase.
    """

    my_substitutions = the_text.maketrans(
        # If you find any of these
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
        # Replace them by these
        "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    return cleaned_text.split()

print(text_to_words("/home/adolfoj/Dev/thinkpython3/src/AliceInWonderland"))
