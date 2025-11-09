import csv
import datetime


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add(self, title, description=""):
        tasks = {"title":title, "description":description, "complete":False}
        self.tasks.append(tasks)
        self.save_task()
        print(f"{title} added")

    def show(self):
        ...

    def complete_task(self):
        ...

    def update_task(self):
        ...

    def filter_task(self):
        ...

    def sort_task(self):
        ...

    def delete_task(self):
        ...

    def save_task(self):
        with open("tasks.csv", mode= "w") as file:
            writer = csv.DictWriter(file, fieldnames=["Title", "Description","Completed"])
            writer.writeheader()
            writer.writerow(self.tasks)

    def load_task(self):
        with open("tasks.csv", mode="r") as file:
            reader = csv.reader()
            for row in reader:
                ord_num, title, description, complete = row
                print(f"{ord_num} {title} {description} {complete}")


def main():
    todolist = ToDoList()
    tit = "test title"
    des = "test description"
    todolist.add(tit,des)


if __name__ == '__main__':
    main()