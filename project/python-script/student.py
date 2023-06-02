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
        print(f"""

        Name: {self.name}
        GPA: {self.gpa}
        Country: {self.country}
        Major: {self.major}
        Gender: {self.gender}
        Code: {self.code}

        """)

    def change_major(self,new_major):
        self.major = new_major

    def change_country(self,new_country):
        self.country = new_country

    def change_name(self,new_name):
        self.name = new_name

    def change_gpa(self,new_gpa):
        self.gpa = new_gpa

    def change_major(self,new_major):
        self.major = new_major