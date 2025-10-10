class Student:
    def __init__(self, sid, name, email, grades=None, courses=None):
        self.id_name = (sid, name)
        self.email = email
        self.grades = grades or {}
        self.courses = set(courses or [])

    def __str__(self):
        return f"ID: {self.id_name[0]}, Name: {self.id_name[1]}, Email: {self.email}, Grades: {self.grades}, Courses: {sorted(self.courses)}"

class StudentRecords:
    def __init__(self):
        self.students = []

    def find(self, sid):
        return next((s for s in self.students if s.id_name[0] == sid), None)

    def add(self, sid, name, email, grades=None, courses=None):
        if self.find(sid): return "Student exists"
        self.students.append(Student(sid, name, email, grades, courses))
        return "Student added"

    def update(self, sid, email=None, grades=None, courses=None):
        s = self.find(sid)
        if not s: return "Not found"
        if email: s.email = email
        if grades: s.grades.update(grades)
        if courses: s.courses.update(courses)
        return "Updated"

    def delete(self, sid):
        s = self.find(sid)
        if not s: return "Not found"
        self.students.remove(s)
        return "Deleted"

    def enroll(self, sid, course):
        s = self.find(sid)
        if not s: return "Not found"
        if course in s.courses: return "Already enrolled"
        s.courses.add(course)
        return "Enrolled"

    def search(self, sid):
        s = self.find(sid)
        return str(s) if s else "Not found"

if __name__ == "__main__":
    r = StudentRecords()
    while True:
        print("\nSelect an option:")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Enroll in Course")
        print("5. Search Student")
        print("6. Exit")
        c = input("Enter your choice (1-6): ")
        if c == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            print(r.add(sid, name, email))
        elif c == "2":
            sid = input("Enter Student ID: ")
            email = input("Enter new Email: ")
            grades = dict(item.split(":") for item in input("Enter Grades: ").split(",") if ":" in item)
            courses_input = input("Enter Courses: ")
            courses = courses_input.split(",") if courses_input else []
            print(r.update(sid, email, grades, courses))
        elif c == "3":
            print(r.delete(input("Enter Student ID to delete: ")))
        elif c == "4":
            print(r.enroll(input("Enter Student ID: "), input("Enter Course to enroll: ")))
        elif c == "5":
            print(r.search(input("Enter Student ID to search: ")))
        elif c == "6":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
