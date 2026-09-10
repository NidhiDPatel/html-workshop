class InvalidMarkError(Exception):
    pass


class Student:
    def __init__(self):
        self.marks = []

    def add_mark(self, mark):
        if mark < 0 or mark > 100:
            raise InvalidMarkError("Invalid mark: " + str(mark))

        self.marks.append(mark)


student = Student()

marks = [85, 92, -10, 75, 105, 88]

for mark in marks:
    try:
        student.add_mark(mark)
        print("Added:", mark)

    except InvalidMarkError as e:
        print("Failed:", e)

print("Valid marks:", student.marks)