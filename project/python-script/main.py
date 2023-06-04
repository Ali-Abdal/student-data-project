import customtkinter
from student_statistics import Statistics
from file import File

# searchs for the studend with desired code then returns the index for the student in the data list
# so I can use this index in other functions related to this specific student
def search_for_student_by_code(students_data, student_code):
    for index, student in enumerate(students_data):
        if student_code == student.code:
            return index
    
    return None

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.file_path = 'project/data/fake-student.csv'
        self.file = File(self.file_path) # make an instance for File class 
        self.students_data = self.file.load_data() # stores file data in a var as a list of Student objects
        self.statistics = Statistics(self.students_data) # make an instance for Statistics class 
        self.wanted_student_index = None # var used to store wanted student index in the list of students data

        # tk
        self.title("Student Info.py")
        self.geometry("700x450")
        

        # tk grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # tk navigation bar
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Student Info",
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.statistics_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Statistics",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.statistics_button_event)
        self.statistics_button.grid(row=1, column=0, sticky="ew")

        self.student_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Student",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.student_button_event)
        self.student_button.grid(row=2, column=0, sticky="ew")

        self.modfiy_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Modify",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.modify_button_event)
        self.modfiy_button.grid(row=3, column=0, sticky="ew")

        # statistics frame
        self.statistics_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.statistics_frame.grid_columnconfigure(0, weight=1)

        self.statistics_menu = customtkinter.CTkOptionMenu(self.statistics_frame, values=['Choose from here!',"Num of students in each country", "Num of students in each major", "Average gpa for each major",
        'Lowest highest gpa for each major','Male and females'],command=self.choose_statistics_menu)
        self.statistics_menu.grid(row=0, column=0, padx=20, pady=(50,20))
        self.statistic_choice = None # var used to store wanted menu value

        self.statistics_textbox= customtkinter.CTkTextbox(self.statistics_frame, width=250)
        self.statistics_textbox.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.statistics_textbox.insert("0.0", "Output:\n\n" )
        
        self.display_button = customtkinter.CTkButton(self.statistics_frame,text="Display", text_color=("gray10", "#DCE4EE"),command=self.display_button_Onclick_listener)
        self.display_button.grid(row=2, column=0, padx=200, pady=(20, 20), sticky="nsew")


        # student frame
        self.student_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.student_frame.grid_columnconfigure(0, weight=1)

        self.student_entry = customtkinter.CTkEntry(self.student_frame, placeholder_text="Please provide us with the student code")
        self.student_entry.grid(row=0, column=0, padx=20, pady=(50,20), sticky="nsew")       

        self.student_menu = customtkinter.CTkOptionMenu(self.student_frame, values=['Choose from here!', 'All student info','Student name',
        'Student country','Student gpa','Student major','Student gender'],command=self.choose_student_menu)
        self.student_menu.grid(row=0, column=1, padx=20, pady=(50,20))
        self.student_choice = None # var used to store wanted menu value


        self.student_textbox= customtkinter.CTkTextbox(self.student_frame, width=250)
        self.student_textbox.grid(row=1, column=0,columnspan=2, padx=20, pady=20, sticky="nsew")
        self.student_textbox.insert("0.0", "Output:\n\n" )
        
        self.student_next_btn = customtkinter.CTkButton(self.student_frame,text="Next", text_color=("gray10", "#DCE4EE"),command=self.student_next_btn_Onclick_listener)
        self.student_next_btn.grid(row=2, column=0,columnspan=2, padx=200, pady=(20, 20), sticky="nsew")


        # modify frame
        self.modify_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.modify_frame.grid_columnconfigure(0, weight=1)

        self.modify_entry = customtkinter.CTkEntry(self.modify_frame, placeholder_text="Entry box")
        self.modify_entry.grid(row=0, column=0, padx=20, pady=(50,20), sticky="nsew")       

        self.modify_menu = customtkinter.CTkOptionMenu(self.modify_frame, values=['Choose from here!', 'Change name','Change gpa',
        'Change country','Change major'],command=self.choose_modify_menu)
        self.modify_menu.grid(row=0, column=1, padx=20, pady=(50,20))
        self.modify_choice = None # var used to store wanted menu value


        self.modify_textbox= customtkinter.CTkTextbox(self.modify_frame, width=250)
        self.modify_textbox.grid(row=1, column=0,columnspan=2, padx=20, pady=20, sticky="nsew")
        self.modify_textbox.insert("0.0", "Output:\n\n" )
        
        self.modify_next_btn = customtkinter.CTkButton(self.modify_frame,text="Next", text_color=("gray10", "#DCE4EE"),command=self.modify_next_btn_Onclick_listener)
        self.modify_next_btn.grid(row=2, column=0,columnspan=2, padx=200, pady=(20, 20), sticky="nsew")

        # select default frame
        self.select_frame_by_name("statistics")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.statistics_button.configure(fg_color=("gray75", "gray25") if name == "statistics" else "transparent")
        self.student_button.configure(fg_color=("gray75", "gray25") if name == "student" else "transparent")
        self.modfiy_button.configure(fg_color=("gray75", "gray25") if name == "modify" else "transparent")

        # show selected frame
        if name == "statistics":
            self.statistics_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.statistics_frame.grid_forget()
        if name == "student":
            self.student_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.student_frame.grid_forget()
        if name == "modify":
            self.modify_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.modify_frame.grid_forget()

    def statistics_button_event(self):
        self.select_frame_by_name("statistics")

    def student_button_event(self):
        self.select_frame_by_name("student")

    def modify_button_event(self):
        self.select_frame_by_name("modify")

    def choose_statistics_menu(self,statistic_choice):
        self.statistic_choice = statistic_choice

    def choose_student_menu(self,student_choice):
        self.student_choice = student_choice

    def choose_modify_menu(self,modify_choice):
        self.modify_choice = modify_choice

    def display_button_Onclick_listener(self):

        if self.statistic_choice == None or self.statistic_choice == 'Choose from here!':
            self.statistics_textbox.delete('0.0','end')
            self.statistics_textbox.insert("0.0", f"Output:\n\nmake sure to choose from the menu above!!!" )                

        if self.statistic_choice == 'Num of students in each country':
            self.statistics_textbox.delete('0.0','end')
            self.statistics_textbox.insert("0.0", f"Output:\n\n{self.statistics.get_num_of_students_in_each_country()}" )

        if self.statistic_choice == 'Num of students in each major':
            self.statistics_textbox.delete('0.0','end')
            self.statistics_textbox.insert("0.0", f"Output:\n\n{self.statistics.get_num_of_students_in_each_major()}" )
            

        if self.statistic_choice == 'Average gpa for each major':
            self.statistics_textbox.delete('0.0','end')
            self.statistics_textbox.insert("0.0", f"Output:\n\n{self.statistics.get_average_gpa_for_each_major()}" )
            

        if self.statistic_choice == 'Lowest highest gpa for each major':
            self.statistics_textbox.delete('0.0','end')
            self.statistics_textbox.insert("0.0", f"Output:\n\n{self.statistics.get_lowest_highest_gpa_for_each_major()}" )
                    

        if self.statistic_choice == 'Male and females':
            self.statistics_textbox.delete('0.0','end')
            self.statistics_textbox.insert("0.0", f"Output:\n\n{self.statistics.get_male_and_females()}" )

    def student_next_btn_Onclick_listener(self):

        if self.student_choice == None or self.student_choice == 'Choose from here!':
            self.student_textbox.delete('0.0','end')
            self.student_textbox.insert("0.0", f"Output:\n\nmake sure to choose from the menu above!!!" )
        else:
            self.student_code = self.student_entry.get()
            self.wanted_student_index = search_for_student_by_code(self.students_data,self.student_code.strip())
            if self.wanted_student_index is not None:
                self.student = self.students_data[self.wanted_student_index]

                if self.student_choice == 'All student info':
                    self.student_textbox.delete('0.0','end')
                    self.student_textbox.insert("0.0", f"Output:\n\n {self.student.describe_student()}" )  

                if self.student_choice == 'Student name':
                    self.student_textbox.delete('0.0','end')
                    self.student_textbox.insert("0.0", f"Output:\n\n Student name: {self.student.name}" )

                if self.student_choice == 'Student country':
                    self.student_textbox.delete('0.0','end')
                    self.student_textbox.insert("0.0", f"Output:\n\n Student country: {self.student.country}" )  

                if self.student_choice == 'Student gpa':
                    self.student_textbox.delete('0.0','end')
                    self.student_textbox.insert("0.0", f"Output:\n\n Student gpa: {self.student.gpa}%" )  

                if self.student_choice == 'Student major':
                    self.student_textbox.delete('0.0','end')
                    self.student_textbox.insert("0.0", f"Output:\n\n Student major: {self.student.major}" ) 

                if self.student_choice == 'Student gender':
                    self.student_textbox.delete('0.0','end')
                    self.student_textbox.insert("0.0", f"Output:\n\n Student gender: {self.student.gender}" )

                self.wanted_student_index = None  
            else:
                    self.student_textbox.delete('0.0','end')
                    self.student_textbox.insert("0.0", f"Output:\n\nCode dosen't exist please make sure that you provided the right code!!" ) 

    def modify_next_btn_Onclick_listener(self):

        if self.modify_choice == None or self.modify_choice == 'Choose from here!':
            self.modify_textbox.delete('0.0','end')
            self.modify_textbox.insert("0.0", f"Output:\n\nmake sure to choose from the menu above!!!" )
        
        elif self.modify_choice == 'Change name' and self.wanted_student_index is not None:
            self.student = self.students_data[self.wanted_student_index]
            name = self.modify_entry.get().title().strip()
            self.student.change_name(name)
            self.file.update_file_data()
            self.modify_textbox.delete('0.0','end')
            self.modify_textbox.insert("0.0", f"Output:\n\nStudent name has been changed to {name}!\n Date file has been updated!" )
            self.wanted_student_index = None

        elif self.modify_choice == 'Change country' and self.wanted_student_index is not None:
            self.student = self.students_data[self.wanted_student_index]
            country = self.modify_entry.get().strip()
            self.student.change_country(country)
            self.file.update_file_data()
            self.modify_textbox.delete('0.0','end')
            self.modify_textbox.insert("0.0", f"Output:\n\nStudent country has been changed to {country}!\n Date file has been updated!" )
            self.wanted_student_index = None

        elif self.modify_choice == 'Change gpa' and self.wanted_student_index is not None:
            self.student = self.students_data[self.wanted_student_index]
            gpa = self.modify_entry.get().strip()
            self.student.change_gpa(gpa)
            self.file.update_file_data()
            self.modify_textbox.delete('0.0','end')
            self.modify_textbox.insert("0.0", f"Output:\n\nStudent gpa has been changed to {gpa}!\n Date file has been updated!" )
            self.wanted_student_index = None

        elif self.modify_choice == 'Change major' and self.wanted_student_index is not None:
            self.student = self.students_data[self.wanted_student_index]
            major = self.modify_entry.get().strip()
            self.student.change_major(major)
            self.file.update_file_data()
            self.modify_textbox.delete('0.0','end')
            self.modify_textbox.insert("0.0", f"Output:\n\nStudent major has been changed to {major}!\n Date file has been updated!" )
            self.wanted_student_index = None
            
        else:
            self.student_code = self.modify_entry.get()
            self.wanted_student_index = search_for_student_by_code(self.students_data,self.student_code.strip())
            if self.wanted_student_index is not None:
                self.student = self.students_data[self.wanted_student_index]

                if self.modify_choice == 'Change name':
                    self.modify_textbox.delete('0.0','end')
                    self.modify_textbox.insert("0.0", f"Output:\n\nPlease type the new name in the entry box then press next." )

                if self.modify_choice == 'Change country':
                    self.modify_textbox.delete('0.0','end')
                    self.modify_textbox.insert("0.0", f"Output:\n\nPlease type the new country in the entry box then press next." )  

                if self.modify_choice == 'Change gpa':
                    self.modify_textbox.delete('0.0','end')
                    self.modify_textbox.insert("0.0", f"Output:\n\nPlease type the new gpa in the entry box then press next." )  

                if self.modify_choice == 'Change major':
                    self.modify_textbox.delete('0.0','end')
                    self.modify_textbox.insert("0.0", f"Output:\n\nPlease type the new major in the entry box then press next." ) 
                        
            else:
                    self.modify_textbox.delete('0.0','end')
                    self.modify_textbox.insert("0.0", f"Output:\n\nCode dosen't exist please make sure that you provided the right code!!" ) 

if __name__ == "__main__":
    app = App()
    app.mainloop()