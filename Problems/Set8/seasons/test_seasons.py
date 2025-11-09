import sys

from season import check_birth_day

def main():
    test_sing()


def test_sing():
    assert check_birth_day("2024-03-04") == [2024, 3, 4]
    assert check_birth_day("July 3, 1998") == None
    assert check_birth_day("january 1, 1999") == None
    return

if __name__ == '__main__':
    main()