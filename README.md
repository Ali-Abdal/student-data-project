# Student data project

Python project that analyses and modify fake data of 1000 students that studies abroad the fake data is generated randomly into a txt file then I cleaned it using a script and stored it in a csv file.

Did this project after taking Python Data Structures course by University of Michigan to implement what I have learned in a real programme.
course link: https://www.coursera.org/learn/python-data

## Brief explenation for the project:
1. First of all method called load_data() from File class reads the csv file and splits the value in each line then stores it in a list of Student objects. 

2. there is 3 sections in the nav bar statistics - student - modify.

3. in statistics frame you will be able to select the wanted method from Statistics class such as getting number of students in each major then when you press the button the output will be shown in the text box.

4. in student frame you will be able to chosse wanted student info from the menu then you will need to provide student's code when you press next button it will checks if the code exist in the data if so it will return wanted student index in the list of data it will display the info 
example: student's major.

5. in modify frame you will be able to change wanted student info for example the student changed his major and you want to change it in the data and in the file you need to choose which value that you want to change then providing wanted student code first it will check if the student exist if so it will ask you to enter the new major then it will change the value both in list of data and in file so if you close the app and reopen it your changes will be saved.

## What I have implemented in this project:
1. looping on tupels, lists and dictionaries
2. unpacking dictionaries as a sorted list of tupels using list comprehensions.
3. lambda function, map function
4. functions
5. classes
6. opening and writing files
7. csv files
8. Tkinter (customtkinter) https://github.com/TomSchimansky/CustomTkinter
9. handling exceptions 

## Demo:

## What I have learned from this project:
1. organizing the code using classes and functions so it become more readable
2. planing and setting tasks in the right order
3. using chat gpt as an assistant with solving problems, explaining new concepts and more ( didn't need stackoverflow at all)
4. Tkinter though it makes the code uglier and messier but it's easy to use and learn and dose the job

# notice:
you will have to install customtkinter
```pip install customtkinter```
