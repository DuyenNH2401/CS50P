import pytest
from um import count

def main():
    pass

def test_lower_upper():
    assert count("hello um how Um do you uM do") == 3
    assert count("Um thank uM kyu um for this umbrella") == 3

def test_part_of_word():
    assert count("yummi") == 0
    assert count("umbrella") == 0

def test_surround_is_space():
    assert count("hello um my um name Um is CS50") == 3
    assert count("um!") == 1