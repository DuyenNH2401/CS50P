import random
import time

start_time = time.time()

b = 0
while True:
    a = random.randint(1, 10000)
    print(a)
    b+=1
    if a == 18:
        break

end_time = time.time()
elapsed =end_time - start_time
print(f"để tìm được giá trị 18 thì ta cần {b} lan random va {elapsed} giay")