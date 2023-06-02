# class to store students data, describe the student & modify the data + the file

class Student:

    def __init__(self,name,gpa,country,major,gender,code):
        self.name = name
        self.gpa = gpa
        self.country = country
        self.major = major
        self.gender = gender
        self.code = code

    def describe_student(self):
        return f"""

        Name: {self.name}
        GPA: {self.gpa}
        Country: {self.country}
        Major: {self.major}
        Gender: {self.gender}
        Code: {self.code}

        """
    