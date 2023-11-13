#Remember: 'import *' means to import all the functions and methods in theis file/package
# you can do '*.md' and this would import all files that end in .md etc.
#e.g. in your terminal if you did 'git add Pipfile *' you'd have to be cause of case sensitivity.

from lib.add_five import *

def test_add_five_returns_eight_for_three():
    result = add_five(3)
    assert result == 8