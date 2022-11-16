"""MX - Simple OOP."""


class Student:
    """Student class."""

    def __init__(self, name: str, finished: bool = False):
        """Initialize the Student class."""
        self.name = name
        self.finished = finished

if __name__ == "__main__":
    student = Student("John")
    print(student.name)
    print(student.finished)
