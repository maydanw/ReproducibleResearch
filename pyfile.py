import sys
import nose

def printme(s):
    s2 = s + '!'
    return s2

def test_printme():
    assert printme('') == '!'

def test_printme2():
    assert printme('123') == '123!'

if __name__ == '__main__':
    # Watch out! Actual code may be coming down ...
    printme('')