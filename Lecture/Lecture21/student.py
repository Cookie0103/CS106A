"""
File: student.py
----------------
The Student class keeps track of the following pieces of data
about a student: the student's name, ID number, and the number
of credits the student has earned toward graduation.
"""


UNITS_TO_GRADUATE = 180     # Constant


class Student:

    def __init__(self, student_name, student_ID):
        """
        Creates a Student object with the given name and ID.
        Initial number of units for a student is 0.
        """
        self.name = student_name
        self.ID = student_ID
        self.units_earned = 0

    def get_name(self):
        """
        Returns the name of the student.
        """
        return self.name

    def get_ID(self):
        """
        Returns the ID number of the student.
        """
        return self.ID

    def get_units(self):
        """
        Returns the number of units earned by this student.
        """
        return self.units_earned

    def set_units(self, units):
        """
        Sets the number of units earned by this student.
        """
        self.units_earned = units

    def increment_units(self, additional_units):
        """
        Adds additional_units to the number of units earned by this student.
        """
        self.units_earned += additional_units

    def can_graduate(self):
        return self.units_earned >= UNITS_TO_GRADUATE
