from unit_tester import test
from wordtools import extract_words


test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
     ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now'])

test(extract_words("she tried to curtsey as she spoke--fancy") ==
     ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy'])
