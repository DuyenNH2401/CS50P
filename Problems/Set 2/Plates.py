def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalnum() and 2<=len(s)<=6:
        num_place = first_num_index(s)
        if  num_place != -1:
            head_sliced = s[0:num_place]
            tail_sliced = s[num_place:]
            if tail_sliced[0] == "0" or not tail_sliced.isnumeric():
                return False
            if not head_sliced.isalpha():
                return False
        else: return True
    else: return False

    return True

def first_num_index(s):
    for index in range(len(s)):
        if s[index].isnumeric():
            return index
    return -1

main()

