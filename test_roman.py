"""
Tests for to_roman function
Author: Poompatai Puntitpong
"""

import roman
import pytest

def test_roman_1():
    assert(roman.to_roman(1876) == 'MDCCCLXXVI')

def test_roman_2():
    assert(roman.to_roman(9784) == 'MMMMMMMMMDCCLXXXIV')
    
def test_roman_3():
    assert(roman.to_roman(949) == 'CMXLIX')

def test_roman_4():
    assert(roman.to_roman(494) == 'CDXCIV')

def test_roman_5():
    assert(roman.to_roman(384) == 'CCCLXXXIV')

def test_roman_6():
    assert(roman.to_roman(237) == 'CCXXXVII')

def test_roman_7():
    assert(roman.to_roman(13) == 'XIII')

def test_roman_8():
    assert(roman.to_roman(5555) == 'MMMMMDLV')

def test_roman_9():
    assert(roman.to_roman(75) == 'LXXV')

def test_roman_10():
    assert(roman.to_roman(9) == 'IX')
	
def test_roman_11():
    with pytest.raises(ValueError):
        roman.to_roman(-10)

def test_roman_12():
    with pytest.raises(ValueError):
        roman.to_roman(-100)

def test_roman_13():
    with pytest.raises(TypeError):
        roman.to_roman('')

def test_roman_14():
    with pytest.raises(TypeError):
        roman.to_roman([])

def test_roman_15():
    with pytest.raises(TypeError):
        roman.to_roman({})