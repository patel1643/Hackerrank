def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] >= 38:
            if (grades[i] + 1)%5 == 0:
              grades[i]+=1
            if (grades[i]+2)%5==0:
              grades[i]+=2            
    return grades
