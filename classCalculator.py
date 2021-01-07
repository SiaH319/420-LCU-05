#Sia Ham (1730812)
#420-LCU Computer Programming , Section 3
#S. Hilal , instructor
#Assignment 2


students = []

def studnet_ID (x,y): #find a student given x in the list of y
        for z in range (len(y)):
                if (x==y[z][1]):
                        return True
        return False

def class_avg (x): # calculate the average  
        average = 0
        for i in range (len(x)):
            for number in range (2, len(x[i])):
                average += x[i][number]
        average = (average/ len(x))
        return average

def letter_grade (z): #giving letter
        if (z >= 87):
                return "A"
        elif(75 <= z <= 86):
                return "B"
        elif(65 <= z <= 74):
                return "C"
        else:
                return "F"
        
def lo_row (x,y): # find row when x is in y
        for z in range (len(y)):
            if (x==y[z][1]):
                return z
        
                       
while True:
        option= input ('''Welcome to the Teacher’s Simple Class Calculator. Here’s the list of options:
                       \n 1- Enter student records (Name, ID, and 6 marks (two test scores and  four assignment scores in order) separated by commas)
                       \n 2- Display the class average.
                       \n 3- Display the total grade, letter grade and relation to class average for a given student\
                       \n 4- Display a simple bar chart to show grade distribution.
                       \n 5- Exit
                       \n Select an option by entering its number or 5 to exit:''')
        
        #option 1:  limit user's tests to 10 students.
        if (option == "1"):
                while len(students) <= 10:#limit the amount of students' information
                        record = input("Enter Student Record of two test scores and four assignment scores (Separate by commas, no spaces) or done: ").split(",")
                        if(len(record) == 8):# check if user gives proper data (ie. Name, ID, and 6 marks separated by commas)
                                for i in range(1, len (record)): #converting to integer
                                        record [i] = int (record [i])
                                if (studnet_ID (record[1], students)):
                                        print ("Duplicate ID. Record rejected.") #each student should have an unique ID
                                else:
                                        students.append (tuple(record))
                                        print ("Record accepted.")
                        elif (record[0] == "done"):
                                break
                        else:
                                print ("Record incomplete. Record rejected.")
                    

        #option 2           
        elif (option == "2"): # calculating class average
                if len(students): #check if any student information is given
                        print ("Class average is ", class_avg(students))
                else:
                        print ("Class average is not calculated since no student information is enetered in the program")
                        
        #option 3    
        elif (option == "3"):
                Name_ID = input ("Enter the name and ID of the student (separate by commas, no spaces):").split(",")
                
                if len(Name_ID) == 2: #check whether the user enetered a valid information (Name, ID)
                        if students: #check if any student information is given in option 1
                                Id = int (Name_ID [1])
                                row = lo_row(Id, students) 
                                stu_avg = int(students [row][2] + students [row][3] + students [row][4] + students [row][5] + students [row][6] + students [row][7])
                                if (class_avg(students) > stu_avg): # calculate the difference between average of a given student and class average
                                        print ("Grade for", students [row][0], "ID=", Id,":", stu_avg, " ", letter_grade(stu_avg), ",", abs(class_avg(students))- stu_avg,"points under the average.")
                                elif (class_avg(students) == stu_avg):
                                        print ("Grade for", students [row][0], "ID=", Id,":", stu_avg, " ", letter_grade(stu_avg), "is the same as the class average.")
                                else:
                                        print ("Grade for", students [row][0], "ID=", Id, ":", stu_avg, " ", letter_grade(stu_avg), ",",  class_avg(students)-stu_avg, "points above the average.")

                        else:
                                print ("full student information should be entered in option 1")
                                
                else:
                        print("Please enter a valid student information")
                
        #opion 4
        elif (option == "4"): #exit program
                print ("A table of the letter grades that correspond to the total score is not required for Assignment 2 ")               
        #opion 5         
        elif (option == "5"): #exit program
                print ("Exit program.")
                break
        
        else: #indicate invalid option
                print ("Please enter a valid option.")



