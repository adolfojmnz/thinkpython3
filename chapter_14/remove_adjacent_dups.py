from get_words_in_book import get_words_in_book

def remove_adjacent_dups(xs):
    """ Return a new list in which all adjacent 
    dupplicates from xs have been removed.
    """
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result
