import random

decks = ["Jack", "King", "Queen"]

print(random.choices(decks,k=2, weights = [99, 1, 0]))
#weights = trọng số để tăng tỉ lệ xuất hiện của phần tử vị trí đó trong decks ban dau
#dung choice or choices để chọn ra 1 hoặc nhiều từ trong 1 lst
#nhưng choices thì có thể bị trùng
print(random.sample(decks,k=2))
#sample giống như choices nhưng không bị trùng
random.seed(0)
#cho vào seed một giá trị thì hàm random.choices hay sample chỉ ra một giá trị duy nhất sau các lần chạy.
