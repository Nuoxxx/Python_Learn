from nose.tools import *
from ex48 import parser

def test_parse_subject():
    result = parser.parse_subject([('verb', 'me')])
    assert_equal(result, ('noun', 'player'))

def test_parse_sentence():
    a = parser.parse_sentence([('verb','eat'),('stop','the'),('noun','bear')])
    assert_equal(a.subject,'player')
    assert_equal(a.verb,'eat')
    assert_equal(a.object,'bear')
