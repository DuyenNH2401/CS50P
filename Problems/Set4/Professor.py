import random


def main():
    level = get_level()
    solved = 0
    score = 0

    while solved < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 0

        while tries < 3:
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        if tries == 3:  # Nếu sai 3 lần, hiển thị kết quả đúng
            print(f"{x} + {y} = {x + y}")

        solved += 1  # Câu hỏi này đã hoàn tất (đúng hoặc sai 3 lần)

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass  # Bỏ qua và yêu cầu nhập lại


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
