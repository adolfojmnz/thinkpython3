def get_words(the_text):
    """
        Return a list of words with al punctuation removed
        with all the letters in lowercase.
    """

    ss = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\"
    ii = "abcdefghijklmnopqrstuvwxyz                                          "

    my_substitutions = the_text.maketrans(
        # If you find any of these
        ss, 
        # Replace them by these
        ii) 

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    return cleaned_text.split()
