import sys
a = 1

print("Hello, my name is", sys.argv[0])
"""
print("Hello, my name is", sys.argv[0])
"""
#sys.exit
print("Chương trình bắt đầu")

# Điều kiện để thoát chương trình
if a < 2:
    print("Thoát chương trình")
    sys.exit(1)  # Thoát với mã thoát 1 (lỗi)

print("Dòng mã này sẽ không được thực hiện nếu sys.exit() được gọi")
