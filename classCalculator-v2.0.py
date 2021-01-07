#Sia Ham (1730812)
#420-LCU Computer Programming , Section 3
#S. Hilal , instructor
#Assignment 3

class Student: 
    'Base class for all students' 
    Count = 0
    CountA =0
    CountB =0
    CountC =0
    CountF =0
    
    def __init__(self,p_name, p_id, p_t1, p_t2, p_a1, p_a2, p_a3, p_a4):
        '''Constructor method'''
        self.name = p_name
        self.id = p_id
        self.t1 = p_t1
        self.t2 = p_t2
        self.a1 = p_a1
        self.a2 = p_a2
        self.a3 = p_a3
        self.a4 = p_a4        
        self.grade = int(p_t1) + int(p_t2) + int(p_a1) + int(p_a2) + int(p_a3) + int(p_a4)
       
        if (self.grade >= 87):
            self.lettergrade = "A"
            Student.CountA +=1
        elif(75 <= self.grade <= 86):
            self.lettergrade = "B"
            Student.CountB +=1
        elif(65 <= self.grade <= 74):
            self.lettergrade = "C"
            Student.CountC +=1
        else:
            self.lettergrade = "F"
            Student.CountF +=1
        
        Student.Count += 1
        
    def __repr__(self):
        return("{:7s}{:7s}{:7d} {:7s} {:7s}{:7s}{:7s}{:7s}{:7s}{:7s}".format(self.id,self.name,self.grade, self.lettergrade, self.t1, self.t2, self.a1,self.a2, self.a3, self.a4))

L = []
while True:
    option= input (''' Welcome to the Teacher’s Simple Class Calculator. Here’s the list of options:
                        \n 1- Read and process Students’ records
                        \n 2- Display All student records
                        \n 3- Display the record of a particular student
                        \n 4- Display the class average and grade distribution.
                        \n 5- Display a simple bar chart to show grade distribution.
                        \n 6- Exit
                        \n Select an option by entering its number or 6 to exit:
                       ''')
    #option 1: Read the text file provided and store student data.
    if (option == "1"):     
        L = []
        fp = open('students.txt')#### students.txt file provided by the instructor should be located in the same folder as my assignment.
        while True: # keep reading
            line = fp.readline()
            if not line: break
            line=line.strip('\n') # remove EOLine
            # Insert code to process and store record here
            record = line.split (',')
            s = Student (record [0], record [1], record [2], record [3], record [4], record [5], record [6], record [7])
            L.append (s)            
        fp.close()


    #option 2: Display all the information stored for each student in a table like format.
    elif (option == "2"):
        if L == []:
            print ("option 1 should be operated first.") 
        else:
            print ("{:7s}{:7s}{:7s} {:7s} {:7s}{:7s}{:7s}{:7s}{:7s}{:7s}".format("Id" , "Name", "T_grade", "L_grade", "t1", "t2", "a1", "a2" , "a3", "a4")) 
            for s in L:
                print (s) #print student info in a table like format

    #option 3: The program will ask the user to enter the name and ID of the student
    elif (option == "3"):
        if L == []:
            print ("option 1 should be operated first.")
        else:
            Name_ID = input ("Enter the NAME of the student first and ID of the student seconde separated by comma (no space between comma):").split(",") 
            c = 0
            if len(Name_ID) ==2:
                for i in L:
                    c += 1      #find the position of the given studnet in L
                    if i.id == Name_ID [1] and i.name == Name_ID [0]:
                        string = "The following is the given student’s record:"
                        print (string)
                        print ("{:7s}{:7s}{:7s} {:7s} {:7s}{:7s}{:7s}{:7s}{:7s}{:7s}".format("Id" , "Name", "T_grade", "L_grade", "t1", "t2", "a1", "a2" , "a3", "a4"))
                        print (L[c-1])
                    else:
                        string = ""
                if not string:
                    print ("Name and ID do not match a stored record.")
            else:
                print ("Please enter a valid information.")
                 
    #opion 4: The class average and grades distribution
    elif (option == "4"):
        if L == []:
            print ("option 1 should be operated first.")
        else:
            total = 0
            count_overav = 0
            for s in L:
                total += s.grade
            average = total / s.Count
            for i in L:
                if i.grade > average:
                    count_overav +=1
            
            print ("The class average is", average)
            print ("The number of students who obtained A is:", s.CountA)
            print ("The number of students who obtained B is:", s.CountB)
            print ("The number of students who obtained C is:", s.CountC)
            print ("The number of students who obtained F is:", s.CountF)
            print ("The number of students who obtained a total grade above the average is:", count_overav )

    #option 5: A graphical distribution of the grades will be displayed.
    elif (option == "5"):
        if L == []:
            print ("option 1 should be operated first.")
        else:        
            import numpy as np      #******module numpy DOES NOT work in .os (it only works in windows at the COMPUTER LAB (**does not work in windows at the library))
            import matplotlib.pyplot as plt
            grades = ("A", "B", "C", "F")
            markings = np.arange (len(grades))
            distribution = [s.CountA, s.CountB, s.CountC,s.CountF] # number of sutdents obtained each letter grade
            plt.bar (markings, distribution, align = 'center', alpha = 0.5)
            plt.xticks (markings, grades) #x axis markings
            plt.title ("Student grades")
            plt.xlabel ("Letter grades")
            plt.ylabel ("Distribution")
            plt.show ()  

    #option 6: exit program

    elif (option == "6"):
        print ("Exit program.")
        break
    else:
        print ("Please choose a valid option")

         
        



