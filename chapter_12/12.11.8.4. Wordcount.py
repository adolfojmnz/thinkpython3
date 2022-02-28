from unit_tester import test
from wordtools import wordcount

test(wordcount("now", ["now", "is", "time", "is", "now", "is", "is"]) == 2)
test(wordcount("is", ["now", "is", "time", "is", "now", "the", "is"]) == 3)
test(wordcount("time", ["now", "is", "time", "is", "now", "is", "is"]) == 1)
test(wordcount("frog", ["now", "is", "time", "is", "now", "is", "is"]) == 0)
