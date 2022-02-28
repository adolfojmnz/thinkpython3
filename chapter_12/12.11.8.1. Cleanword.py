from unit_tester import test
from wordtools import cleanword

test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") == "word")
