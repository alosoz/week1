# 2.Course Score Calculation
# User Name, Surname, Student Number, 4 course names, Visa and Final grades will be required. 
# The sum of 40% of the midterm grade and 60% of the final grade will give the year-end average. 
# If the average is less than 50, “FAILED” on the screen, 50 and above, “PASSED” will be printed on the screen. 
# This printing process is in 4 lessons. will be done and the lessons will be written one after the other.



user_name = input("Name: ") 
surname = input("Surname: ")
student_number = input("Student Number: ") 

course = ["Art","History","Science","Math"]


for lesson in course:
    visa = float(input(lesson +" Visa: "))
    final = float(input(lesson +" Final: "))

    year_average = ((visa*40)/100) + ((final*60)/100)
    
    if year_average < 50:
        print(lesson + ": Failed")
    elif year_average >= 50:
        print(lesson + ": Passed")
