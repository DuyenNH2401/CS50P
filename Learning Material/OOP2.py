
class Students:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name} from {self.grade}"


def main():
    student = get_student()
    print(student)

if __name__ == '__main__':
    main()