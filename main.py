from student import Student
from group import Group

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert gr.find_student('Jobs') == st1, f"Expected {st1}, but got {gr.find_student('Jobs')}"
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)  # Only one student should remain

gr.delete_student('Taylor')  # No error!

import os
import zipfile

os.makedirs('project', exist_ok=True)

with open('project/student.py', 'w') as f:
    f.write('''class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Record Book: {self.record_book}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
        return hash(str(self))
''')

with open('project/group.py', 'w') as f:
    f.write('''from student import Student

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise ValueError("Group cannot have more than 10 students")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\\n'.join(str(student) for student in self.group)
        return f"Number: {self.number}\\n{all_students}"
''')

with open('project/main.py', 'w') as f:
    f.write('''from student import Student
from group import Group

# Створення студентів
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

# Створення групи
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

# Виведення групи
print(gr)

# Тести
assert gr.find_student('Jobs') == st1, f"Expected {st1}, but got {gr.find_student('Jobs')}"
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)  # Only one student should remain

# Перевірка видалення неіснуючого студента
gr.delete_student('Taylor')  # No error!
''')

with zipfile.ZipFile('project.zip', 'w') as zipf:
    for folder, subfolders, files in os.walk('project'):
        for file in files:
            zipf.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), 'project'))
