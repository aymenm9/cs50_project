from sqlalchemy import Column, Integer, String, ForeignKey, relationship, JSON
from db import db
class Admin(db.Model):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<Admin(id={self.id}, username='{self.username}')>"


class Department(db.Model):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    levels = relationship("Level", backref="department")  # One department has many levels


class Level(db.Model):
    __tablename__ = 'level'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'))

    classes = relationship("Class", backref="level")  # One level has many classes
    subjects = relationship("Subject", secondary="level_subject")  # Many-to-Many with Subject


class Class(db.Model):
    __tablename__ = 'class'

    id = Column(Integer, primary_key=True, autoincrement=True)
    class_number = Column(Integer, nullable=False)
    level_id = Column(Integer, ForeignKey('level.id'))

    students = relationship("Student", backref="classs")  # One class has many students
    teachers_subjects = relationship(
        "TeacherClassSubject", backref="class_"
    )  # One class has many teacher-subject relationships


class Teacher(db.Model):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)

    teachers_subjects = relationship(
        "TeacherClassSubject", backref="teacher"
    )  # One teacher has many teacher-subject relationships


class Student(db.Model):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    full_name = Column(String(50))
    class_id = Column(Integer, ForeignKey('class.id'))

    grades = relationship("Grade", backref="student")  # One student has many grades


class Subject(db.Model):
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    level_id = Column(Integer, ForeignKey('level.id'))
    coefs = Column(JSON)  # Can be a dictionary or list representing coefficients

    levels = relationship("Level", secondary="level_subject")  # Many-to-Many with Level


class LevelSubject(db.Model):
    __tablename__ = 'level_subject'

    level_id = Column(Integer, ForeignKey('level.id'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subject.id'), primary_key=True)
    coef = Column(Integer)


class TeacherClassSubject(db.Model):
    __tablename__ = 'teacher_class_subject'

    teacher_id = Column(Integer, ForeignKey('teacher.id'), primary_key=True)
    class_id = Column(Integer, ForeignKey('class.id'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subject.id'), primary_key=True)