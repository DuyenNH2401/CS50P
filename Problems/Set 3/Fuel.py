while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        res = x / y
        percent = int(round(res * 100))
        if percent <= 100:
            break
    except (ZeroDivisionError, ValueError):
        pass

if percent <= 1:
    print("E")
elif percent >=99:
    print("F")
else: print(f"{percent}%")
