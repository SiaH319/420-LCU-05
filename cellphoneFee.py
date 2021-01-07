#Sia Ham (1730812)
#420-LCU Computer Programming , Section 3
#Monday , September 17th
#S. Hilal , instructor
#Assignment 1

#Exercise 2.

x=int(input("Number of daytime minutes?"))
y=int(input("Number of evening minutes?"))
c=int(input("Number of weekend minutes?"))


if x<=100:                      #Define the cost of daytime uses of Plan A 
    DaytimeA = 0                #If the daytime uses is less than or equal to 100 (minutes), it is ignored
elif x>100:
    DaytimeA = 0.15 * (x-100)        

EveningA = y*0.20               #Define the cost of evening uses of Plan A
WeekendA = c*0.25               #Define the cost of weekend uses of Plan A

PlanA = DaytimeA + EveningA + WeekendA + 10      #Define Plan A



if x<=200:                      #Define the cost of daytime uses of Plan B
    DaytimeB = 0                #If the daytime uses is less than or equal to 200 (minutes), it is ignored
elif x>200:
    DaytimeB = 0.20 * (x-200)

EveningB = y*0.25               #Define the cost of evening uses of Plan B
WeekendB = c*0.30               #Define the cost of weekend uses of Plan B

PlanB = DaytimeB + EveningB + WeekendB + 10      #Define Plan B



if x<=250:                      #Define the cost of daytime uses of Plan C
    DaytimeC = 0                #If the daytime uses is less than or equal to 250 (minutes), it is ignored
elif x>250:
    DaytimeC = 0.30 * (x-250)

EveningC = y*0.35              #Define the cost of evening uses of Plan C
WeekendC = c*0.40              #Define the cost of weekend uses of Plan C

PlanC = DaytimeC + EveningC + WeekendC + 10      #Define Plan C


print("Plan A cost (in $)", "%0.2f"%PlanA)  
print("Plan B cost (in $)", "%0.2f"%PlanB)
print("Plan C cost (in $)", "%0.2f"%PlanC)

if PlanA < PlanB and PlanA < PlanC:
    cheapest = "A."
elif PlanB < PlanA and PlanB < PlanC:
    cheapest = "B."
elif PlanC < PlanA and PlanC < PlanB:
    cheapest = "C."
elif PlanA == PlanB:
    cheapest = "A or B."
elif PlanA == PlanC:
    cheapest = "A or C."
elif PlanB == PlanC:
    cheapest = "B or C."
elif PlanA == PlanB == PlanC:
    cheapest = "A or B or C."
print ("Choose Plan", cheapest)
