from student import Student
import csv

class File:
    def __init__(self,file_path):
        self.file_path = file_path
        self.students_data = None

    # loads the data from the csv file and stores it in a list of Student objects
    def load_data(self):
        try:
            with open(self.file_path,'r') as fh:
                self.students_data = []
                next(fh)
                for line in fh:
                    student_data = line.split(',')
                    name = student_data[0]
                    major = student_data[1]
                    country = student_data[2]
                    gpa = student_data[3]
                    gender = student_data[4]
                    code = student_data[5].strip()
                    self.students_data.append(Student(name,gpa,country,major,gender,code))
                print('Data has been uploaded!')
                return self.students_data
        except FileNotFoundError:
            print('Error check the file path main function in main.py!!!')

    def update_file_data(self):
        with open(self.file_path,'w') as fh:
            writer = csv.writer(fh)
            writer.writerow(['name','major','country','gpa','gender','code'])
            for student in self.students_data:
                writer.writerow([student.name,student.major,student.country,student.gpa,student.gender,student.code])
        print('File data has been updated!')