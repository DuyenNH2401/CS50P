import random

def main():
    level = get_level()
    num = random.randint(1, level)
    guesss = guess(num)
    if guesss == num:
        print("Just right!")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 1:
                return level
        except:
            pass

def guess(num):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 0:
                continue
            elif guess > num:
                print("Too large!")
                continue
            elif guess < num:
                print("Too small!")
                continue
            elif guess == num:
                return guess
        except:
            pass

if __name__ == '__main__':
    main()