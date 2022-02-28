def count_words(book):
    output = {}
    
    for word in book:
        if word != 'n':
            output[word] = output.get(word, 0) + 1
    return output