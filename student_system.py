from abc import ABC, abstractmethod
from typing import List


# 1. Abstract Base Class (Inheritance & Polymorphism)
class UniversityMember(ABC):
    def __init__(self, member_id: str, full_name: str, email: str):
        self._member_id = member_id
        self._full_name = full_name
        self._email = email

    @property
    def full_name(self) -> str:
        return self._full_name

    @abstractmethod
    def get_role_summary(self) -> str:
        pass


# 2. Subclass: Student (Inherits from UniversityMember)
class Student(UniversityMember):
    def __init__(self, member_id: str, full_name: str, email: str, major: str, academic_year: int):
        super().__init__(member_id, full_name, email)
        self.__major = major
        self.__academic_year = academic_year
        self.__records: List['GradeRecord'] = []

    def add_grade_record(self, record: 'GradeRecord') -> None:
        self.__records.append(record)

    def calculate_gpa(self) -> float:
        if not self.__records:
            return 0.0
        total_points = sum(r.grade_point * r.subject.credits for r in self.__records)
        total_credits = sum(r.subject.credits for r in self.__records)
        return round(total_points / total_credits, 2) if total_credits > 0 else 0.0

    def get_role_summary(self) -> str:
        return f"[Student] {self._full_name} (ID: {self._member_id}) | Major: {self.__major} | Year: {self.__academic_year} | GPA: {self.calculate_gpa()}"


# 3. Subclass: Advisor (Inherits from UniversityMember)
class Advisor(UniversityMember):
    def __init__(self, member_id: str, full_name: str, email: str, office_number: str):
        super().__init__(member_id, full_name, email)
        self.__office_number = office_number
        self.__advisees: List[Student] = []

    def assign_student(self, student: Student) -> None:
        self.__advisees.append(student)

    def get_role_summary(self) -> str:
        return f"[Advisor] Dr. {self._full_name} | Office: {self.__office_number} | Advisees Count: {len(self.__advisees)}"


# 4. Subject Class (Part of Composition with Faculty)
class Subject:
    def __init__(self, subject_code: str, title: str, credits: int):
        self.subject_code = subject_code
        self.title = title
        self.credits = credits

    def __str__(self) -> str:
        return f"{self.subject_code}: {self.title} ({self.credits} Credits)"


# 5. Association Class: GradeRecord (Links Student and Subject)
class GradeRecord:
    def __init__(self, student: Student, subject: Subject, score: float, semester: str):
        self.student = student
        self.subject = subject
        self.score = score
        self.semester = semester
        self.grade_point = self._convert_to_gpa_scale(score)
        student.add_grade_record(self)

    @staticmethod
    def _convert_to_gpa_scale(score: float) -> float:
        if score >= 90:
            return 4.0
        elif score >= 80:
            return 3.5
        elif score >= 70:
            return 3.0
        elif score >= 60:
            return 2.0
        return 0.0


# 6. Faculty Class (Composition with Subject & Aggregation with Advisor)
class Faculty:
    def __init__(self, faculty_name: str):
        self.faculty_name = faculty_name
        self.__subjects: List[Subject] = []
        self.__advisors: List[Advisor] = []

    # Composition: Faculty creates and owns its subjects
    def create_subject(self, code: str, title: str, credits: int) -> Subject:
        new_subject = Subject(code, title, credits)
        self.__subjects.append(new_subject)
        return new_subject

    # Aggregation: Advisors exist independently and join the faculty
    def add_advisor(self, advisor: Advisor) -> None:
        self.__advisors.append(advisor)

    def display_faculty_overview(self) -> None:
        print(f"=== {self.faculty_name} ===")
        print(f"Offered Subjects: {len(self.__subjects)} | Active Advisors: {len(self.__advisors)}\n")


# --- Main Execution & Testing ---
if __name__ == "__main__":
    # Create Faculty
    cs_faculty = Faculty("Faculty of Computing & Information Technology")

    # Composition: Create Subjects inside Faculty
    sub1 = cs_faculty.create_subject("CS201", "Object-Oriented Programming", 3)
    sub2 = cs_faculty.create_subject("CS205", "Software Engineering", 4)

    # Aggregation: Create Advisor and attach to Faculty
    advisor1 = Advisor("ADV-101", "Tariq Al-Mansoor", "t.almansoor@uni.edu", "Bldg 3 - Room 204")
    cs_faculty.add_advisor(advisor1)

    # Create Students
    student1 = Student("STU-202601", "Omar Khalid", "omar.k@uni.edu", "Software Engineering", 2)
    student2 = Student("STU-202602", "Sara Ahmed", "sara.a@uni.edu", "Computer Science", 3)

    # Assign Students to Advisor
    advisor1.assign_student(student1)
    advisor1.assign_student(student2)

    # Association: Record Student Grades
    GradeRecord(student1, sub1, 92.0, "Fall 2026")
    GradeRecord(student1, sub2, 85.0, "Fall 2026")
    GradeRecord(student2, sub1, 78.0, "Fall 2026")

    # Display Output (Polymorphism in action)
    cs_faculty.display_faculty_overview()
    members: List[UniversityMember] = [advisor1, student1, student2]
    for member in members:
        print(member.get_role_summary())