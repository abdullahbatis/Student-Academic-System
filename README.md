# Student Academic Management System — Mapping Design to Code

## Overview
This repository implements a UML Class Diagram for a **Student Academic Management System** using **Python 3**. It demonstrates how object-oriented design structures and class relationships translate directly into clean, maintainable source code.

## Class Diagram Architecture

The system consists of **6 classes**:

| Class | Type | Responsibility |
| :--- | :--- | :--- |
| **`UniversityMember`** | Abstract Class | Base class defining common identity attributes and abstract `get_role_summary()` method. |
| **`Student`** | Concrete Class | Inherits from `UniversityMember`; stores major, year, grade records, and computes GPA. |
| **`Advisor`** | Concrete Class | Inherits from `UniversityMember`; manages assigned student advisees and office details. |
| **`Faculty`** | Concrete Class | Represents an academic faculty that owns subjects and manages advisors. |
| **`Subject`** | Concrete Class | Represents an academic course/subject with credit hours. |
| **`GradeRecord`** | Association Class | Connects `Student` and `Subject` with exam scores, semester info, and GPA points. |

## Mapped UML Relationships
- **Inheritance:** `UniversityMember` ◁── `Student`, `Advisor`
- **Association:** `Student` ─── `GradeRecord` ─── `Subject`
- **Composition:** `Faculty` ◆── `Subject` *(Subjects are created and owned by the Faculty)*
- **Aggregation:** `Faculty` ◇── `Advisor` *(Advisors can exist independently of a specific Faculty)*

## How to Run
Make sure Python 3.8+ is installed, then run:
```bash
python student_system.py