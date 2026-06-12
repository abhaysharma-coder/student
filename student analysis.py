"""
========================================================
   STUDENT MANAGEMENT SYSTEM
   Built with Python & Object-Oriented Programming (OOP)
========================================================
"""


# ─────────────────────────────────────────────
#  CLASS: Student
# ─────────────────────────────────────────────
class Student:
    """Represents a single student with ID, name, age, and marks."""

    def __init__(self, student_id: str, name: str, age: int, marks: float):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self) -> str:
        return (
            f"  ID     : {self.student_id}\n"
            f"  Name   : {self.name}\n"
            f"  Age    : {self.age}\n"
            f"  Marks  : {self.marks}"
        )


# ─────────────────────────────────────────────
#  CLASS: StudentManagementSystem
# ─────────────────────────────────────────────
class StudentManagementSystem:
    """Core system that manages a collection of Student objects."""

    def __init__(self):
        self._students: list[Student] = []   # private list to store students

    # ── helpers ───────────────────────────────
    def _print_divider(self, char: str = "─", width: int = 50) -> None:
        print(char * width)

    def _find_student(self, student_id: str) -> Student | None:
        """Return the Student object with the given ID, or None."""
        for student in self._students:
            if student.student_id == student_id:
                return student
        return None

    def _id_exists(self, student_id: str) -> bool:
        return self._find_student(student_id) is not None

    # ── 1. Add a new student ──────────────────
    def add_student(self) -> None:
        self._print_divider()
        print("         ➕  ADD NEW STUDENT")
        self._print_divider()

        student_id = input("  Enter Student ID   : ").strip()
        if not student_id:
            print("  ❌  Student ID cannot be empty.")
            return
        if self._id_exists(student_id):
            print(f"  ❌  Student with ID '{student_id}' already exists.")
            return

        name = input("  Enter Name         : ").strip()
        if not name:
            print("  ❌  Name cannot be empty.")
            return

        try:
            age = int(input("  Enter Age          : "))
            if age <= 0:
                raise ValueError
        except ValueError:
            print("  ❌  Please enter a valid positive integer for age.")
            return

        try:
            marks = float(input("  Enter Marks (0–100): "))
            if not (0 <= marks <= 100):
                raise ValueError
        except ValueError:
            print("  ❌  Marks must be a number between 0 and 100.")
            return

        student = Student(student_id, name, age, marks)
        self._students.append(student)
        print(f"\n  ✅  Student '{name}' added successfully!")

    # ── 2. View all students ──────────────────
    def view_students(self) -> None:
        self._print_divider()
        print("         📋  ALL STUDENTS")
        self._print_divider()

        if not self._students:
            print("  ⚠️   No students found. Add some students first.")
            return

        for index, student in enumerate(self._students, start=1):
            print(f"\n  [{index}]")
            print(student)
        print()

    # ── 3. Search for a student ───────────────
    def search_student(self) -> None:
        self._print_divider()
        print("         🔍  SEARCH STUDENT")
        self._print_divider()

        student_id = input("  Enter Student ID to search: ").strip()
        student = self._find_student(student_id)

        if student:
            print("\n  ✅  Student Found:\n")
            print(student)
        else:
            print(f"  ❌  No student found with ID '{student_id}'.")

    # ── 4. Update marks ───────────────────────
    def update_marks(self) -> None:
        self._print_divider()
        print("         ✏️   UPDATE STUDENT MARKS")
        self._print_divider()

        student_id = input("  Enter Student ID   : ").strip()
        student = self._find_student(student_id)

        if not student:
            print(f"  ❌  No student found with ID '{student_id}'.")
            return

        print(f"\n  Current Marks for {student.name}: {student.marks}")
        try:
            new_marks = float(input("  Enter New Marks (0–100): "))
            if not (0 <= new_marks <= 100):
                raise ValueError
        except ValueError:
            print("  ❌  Marks must be a number between 0 and 100.")
            return

        old_marks = student.marks
        student.marks = new_marks
        print(
            f"\n  ✅  Marks updated for '{student.name}':"
            f" {old_marks} → {new_marks}"
        )

    # ── 5. Delete a student ───────────────────
    def delete_student(self) -> None:
        self._print_divider()
        print("         🗑️   DELETE STUDENT")
        self._print_divider()

        student_id = input("  Enter Student ID to delete: ").strip()
        student = self._find_student(student_id)

        if not student:
            print(f"  ❌  No student found with ID '{student_id}'.")
            return

        confirm = input(
            f"  Are you sure you want to delete '{student.name}'? (yes/no): "
        ).strip().lower()

        if confirm == "yes":
            self._students.remove(student)
            print(f"\n  ✅  Student '{student.name}' deleted successfully.")
        else:
            print("  ℹ️   Deletion cancelled.")

    # ── 6. Highest marks student ──────────────
    def highest_marks_student(self) -> None:
        self._print_divider()
        print("         🏆  STUDENT WITH HIGHEST MARKS")
        self._print_divider()

        if not self._students:
            print("  ⚠️   No students found. Add some students first.")
            return

        top_student = max(self._students, key=lambda s: s.marks)
        print("\n  🎖️  Top Performer:\n")
        print(top_student)
        print()


# ─────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────
def display_menu() -> None:
    print()
    print("=" * 50)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("  1️⃣   Add New Student")
    print("  2️⃣   View All Students")
    print("  3️⃣   Search Student by ID")
    print("  4️⃣   Update Student Marks")
    print("  5️⃣   Delete Student Record")
    print("  6️⃣   Display Highest Marks Student")
    print("  7️⃣   Exit")
    print("=" * 50)


def main() -> None:
    sms = StudentManagementSystem()

    print("\n  Welcome to the Student Management System!")

    while True:
        display_menu()
        choice = input("  👉  Enter your choice (1–7): ").strip()

        if choice == "1":
            sms.add_student()
        elif choice == "2":
            sms.view_students()
        elif choice == "3":
            sms.search_student()
        elif choice == "4":
            sms.update_marks()
        elif choice == "5":
            sms.delete_student()
        elif choice == "6":
            sms.highest_marks_student()
        elif choice == "7":
            print("\n  👋  Thank you for using the Student Management System. Goodbye!\n")
            break
        else:
            print("\n  ❌  Invalid choice. Please enter a number between 1 and 7.")

        input("\n  Press Enter to continue...")


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()
      