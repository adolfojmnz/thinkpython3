from unit_tester import test
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

all_words = get_words_in_book('AliceInWonderland.txt')
all_words.sort()
book_words = remove_adjacent_dups(all_words)
print(
    f'There are {len(all_words)} words in the book. '
    f'Only {len(book_words)} words are unique.')
print(f'The first 10 words are: \n {book_words[:10]}')


test(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
test(remove_adjacent_dups([]) == [])
test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) ==
                                   ["a", "big", "bite", "dog"])

