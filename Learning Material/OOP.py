
class Students:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name} from {self.grade}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if grade not in ["10", "11", "12"]:
            raise ValueError
        self._grade = grade

def main():
    student = get_student()
    student._grade = "9"
    print(student)

def get_student():
    name = input("Name: ")
    grade = str(input("Grade: "))
    return Students(name, grade)

if __name__ == '__main__':
    main()