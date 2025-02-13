from typing import Dict, List, Union

contacts: Dict[str, Union[int, List[Dict[str, str]]]] = {
    "number": 4,
    "students": [
        {"name": "Sarah Holderness", "email": "sarah@example.com"},
        {"name": "Harry Potter", "email": "harry@example.com"},
        {"name": "Hermione Granger", "email": "hermione@example.com"},
        {"name": "Ron Weasley", "email": "ron@example.com"},
    ],
}

print("Student emails:")
students = contacts.get("students")
if isinstance(students, list):
    for student in students:
        print(student["email"])
