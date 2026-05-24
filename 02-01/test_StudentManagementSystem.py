import pytest
from StudentManagement import (
    SchoolManagementSystem,
    StudentNotFoundError,
    SubjectNotFoundError,
    DuplicateStudentError,
)

# ---------- FIXTURE ----------
@pytest.fixture
def sms():
    return SchoolManagementSystem()


# ---------- ADD STUDENT ----------
def test_add_student_success(sms):
    sms.add_student("101", "Lokesh", "10A")
    assert "101" in sms.students


def test_add_duplicate_student(sms):
    sms.add_student("101", "Lokesh", "10A")
    with pytest.raises(DuplicateStudentError):
        sms.add_student("101", "Raj", "10B")


# ---------- ADD MARKS ----------
def test_add_marks_success(sms):
    sms.add_student("102", "Anu", "9B")
    sms.add_marks("102", "Maths", 90)
    assert sms.students["102"].marks["Maths"] == 90


def test_add_marks_invalid_student(sms):
    with pytest.raises(StudentNotFoundError):
        sms.add_marks("999", "Maths", 80)


# ---------- UPDATE MARKS ----------
def test_update_marks_success(sms):
    sms.add_student("103", "Kiran", "8A")
    sms.add_marks("103", "Science", 75)
    sms.update_marks("103", "Science", 85)
    assert sms.students["103"].marks["Science"] == 85


def test_update_marks_invalid_subject(sms):
    sms.add_student("104", "Ravi", "7C")
    with pytest.raises(SubjectNotFoundError):
        sms.update_marks("104", "English", 70)


def test_update_marks_invalid_student(sms):
    with pytest.raises(StudentNotFoundError):
        sms.update_marks("999", "Maths", 60)


# ---------- DISPLAY STUDENT ----------
def test_display_student_invalid_id(sms):
    with pytest.raises(StudentNotFoundError):
        sms.display_student_info("888")