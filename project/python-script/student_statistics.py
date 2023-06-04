# class with mathmatical methods to get info from the data

class Statistics:
    
    def __init__(self,students_data):
        self.students_data = students_data


    # counts how many each country is repeated then prints the country name with the number of students studing
    # in descending order
    def get_num_of_students_in_each_country(self):
        count = {}
        for student in self.students_data:
            count[student.country] = count.get(student.country,0) + 1 
    
        tmp = sorted(((v,k) for k,v in count.items()),reverse=True) # k = country, v = number of students

        output = ''
        for number_of_students,country in tmp:
            output += f'{country}: {number_of_students} students\n'
    
        return output


    # counts how many each major is repeated then prints the major name with the number of students studing
    # in descending order
    def get_num_of_students_in_each_major(self):
        count = {}
        for student in self.students_data:
            count[student.major] = count.get(student.major,0) + 1
    
        tmp = sorted(((v,k) for k,v in count.items()),reverse=True) # k = major, v = number of students

        output = ''
        for number_of_students,major in tmp:
            output += f'{major}: {number_of_students} students\n'

        return output   


    # gets total gpa for each major assiened to a key with major name in a dictionary then counts the number of students in each 
    # major then prints the major name with the average gpa in descending order
    def get_average_gpa_for_each_major(self):

        total_gpa_for_each_major = {}
        count = {}
        for student in self.students_data:
            total_gpa_for_each_major[student.major] = total_gpa_for_each_major.get(student.major,0) + float(student.gpa)
            count[student.major] = count.get(student.major,0) + 1

        total_gpa_for_each_major = sorted([(k,v) for k,v in total_gpa_for_each_major.items()])
        count = sorted([(k,v) for k,v in count.items()])

        # x[0] = major, x[1] = total gpa, n[1] = number of students
        major_data = list(map(lambda x,n: (x[0],x[1],int(n[1])),total_gpa_for_each_major,count))

        # n = number of students, m = major, t = total gpa
        major_data = sorted([(n/t,m) for m,n,t in major_data ],reverse=True)

        output = ''
        for (average_gpa,major) in major_data:
            output += f'{major}: {round(average_gpa,2)}%\n'

        return output


    # makes a dictionary contains majors as a key assigend to list of accepted students gpas in that major then prints
    # the lowest gpa and the highest gpa
    def get_lowest_highest_gpa_for_each_major(self):
        gpa_for_each_major = {}
        for student in self.students_data:
            gpa_for_each_major[student.major] = gpa_for_each_major.get(student.major,[])
            gpa_for_each_major[student.major].append(float(student.gpa))
        
        output = ''
        for major,gpa in gpa_for_each_major.items():
            tmp_lst = [ x for x in gpa]
            output += f'{major}: L {min(tmp_lst)}% H {max(tmp_lst)}%\n'
        
        return output

    # makes a dictionary contains gender as key assiend to total of student from both gender then prints it
    def get_male_and_females(self):
        count = {}
        for student in self.students_data:
            count[student.gender.strip()] = count.get(student.gender.strip(),0) + 1
        
        output = f'Total: {len(self.students_data)}\nMale: {count["Male"]}\nFemale: {count["Female"]}'        
        return output
        