from lib.counter import *
def test_no_counted_to_zero():
    counter = Counter()
    counter.add(0)
    assert counter.count == 0

def test_reporting_counter():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

