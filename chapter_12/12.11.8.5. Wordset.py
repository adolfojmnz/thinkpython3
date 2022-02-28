from unit_tester import test
from wordtools import wordset


test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
     ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
     ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
     ["a", "am", "are", "be", "but", "is", "or"])
