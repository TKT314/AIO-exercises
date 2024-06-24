from abc import ABC, abstractmethod
import torch.nn as nn
import torch


#1. Viết class và cài phương thức softmax
class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        return x_exp / torch.sum(x_exp)
#2. 
#câu a
class Student:
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        return f"Student(Name: {self.name}, Year of Birth: {self.yob}, Grade: {self.grade})"


class Doctor:
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        return f"Doctor(Name: {self.name}, Year of Birth: {self.yob}, Specialist: {self.specialist})"


class Teacher:
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        return f"Teacher(Name: {self.name}, Year of Birth: {self.yob}, Subject: {self.subject})"
#câu b;c;d;e
class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        ward_info = f"Ward Name: {self.name}\n"
        for person in self.people:
            ward_info += person.describe() + "\n"
        return ward_info
    def count_doctor(self):
        return sum(isinstance(person, Doctor) for person in self.people)
    def sort_age(self):
        self.people.sort(key=lambda person: person.yob)
    def compute_average(self):
        teachers = [person for person in self.people if isinstance(person, Teacher)]
        if not teachers:
            return 0
        return sum(teacher.yob for teacher in teachers) / len(teachers)
#câu 3
class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.element = []
    
    def is_empty(self):
        return len(self.element) == 0
    
    def is_full(self):
        return len(self.element) == self.capacity
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.element.pop()
    
    def push(self, value):
        if self.is_full():
            raise OverflowError("Push to full stack")
        self.element.append(value)
    
    def top(self):
        if self.is_empty():
            raise IndexError("Top from empty stack")
        return self.element[-1]
class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def is_full(self):
        return len(self.elements) == self.capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.elements.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Enqueue to full queue")
        self.elements.append(value)

    def front(self):
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.elements[0]
if __name__ == "__main__":
    student1 = Student(name="studentA", yob=2010, grade="7")
    print(student1.describe())

    # Tạo ward object và thêm vào 1 student, 2 teacher, và 2 doctor
    ward = Ward("Central Ward")
    ward.add_person(Student("Alice", 2005, "10th Grade"))
    ward.add_person(Teacher("Mr. Smith", 1980, "Math"))
    ward.add_person(Teacher("Ms. Johnson", 1975, "History"))
    ward.add_person(Doctor("Dr. Brown", 1970, "Cardiology"))
    ward.add_person(Doctor("Dr. Green", 1985, "Neurology"))
    print(ward.describe())
    print(f"Number of doctors in ward: {ward.count_doctor()}")
    ward.sort_age()
    print(ward.describe())
    average_yob = ward.compute_average()
    print(f"Average Year of Birth of Teachers: {average_yob}")

    stack1 = MyStack ( capacity =5)
    stack1.push (1)
    stack1.push (2)
    print ( stack1 . is_full () )
    print ( stack1 . top () )
    print ( stack1 . pop () )

    queue1 = MyQueue ( capacity =5)
    queue1 . enqueue (1)
    queue1 . enqueue (2)
    print ( queue1 . is_full () )
    print ( queue1 . front () )
    print ( queue1 . dequeue () )
    print ( queue1 . front () )
    print ( queue1 . dequeue () )
    print ( queue1 . is_empty () )