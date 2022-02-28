from unit_tester import test
from wordtools import has_dashdash

test(has_dashdash("distance--but"))
test(not has_dashdash("several")) # False and then True, du the not operator
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))
# The last statement recive a True from the function call 
# and then it is denied.
