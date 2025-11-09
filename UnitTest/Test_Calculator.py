from CS50P.UnitTest.Calculator import square
def main():
    test_square()
def test_square():
#Kiểm tra thông thường
#    if square(2) != 4:
#        print("Hàm sai")
#    else:
#        print("Hàm đã chính xác")
#Kiểm tra bằng assert
    assert square(2)==4
    assert square(3)==6

if __name__ == "__main__":
    main()