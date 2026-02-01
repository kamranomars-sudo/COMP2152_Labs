grades = [85, 92, 78, 95, 88]
grades.append(90)
grades.sort()
print(f"Sorted Grades: {grades}") #Sorted Grades: [78, 85, 88, 90, 92, 95]      
print(f"Highest Grade: {grades[-1]}")
print(f"Lowest Grade: {grades[0]}")
print(f"Total number of Grade: {len(grades)}")
