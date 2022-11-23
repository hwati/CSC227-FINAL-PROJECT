# Hagar is a sample student, and idlist and studentlist are populated with sample testable entries
from resources.Student import Student


hagar = Student("hagar", "1", ["CSC130", "CSC227"])


# IDList is a dict with items structured {"ID number": "Password"}
IDList = { hagar.id: "1"}

# studentlist is a dict with items structured {"ID number": Student object}
studentlist = {hagar.id: hagar}
