grado = []

while True:
    input_grade = input("Enter the grade: ")
    
    if input_grade.lower() == "done":
        break
    
    try:
        grade = float(input_grade)
        
        if 40 < grade < 100:
            grado.append(grade)
        else:
            print("Invalid grade, must be between 40 and 100 only.")
    except ValueError:
        print("Invalid input, please enter a number or 'done' to finish.")
        
if grado:
    average_grade = sum(grado) / len(grado)
    print(f"\nAverage Grade: {sum(grado)} / {len(grado)} = {average_grade:.2f}")
else:
    print("Nothing input")

passing_grade = 75
passed_students = [grade for grade in grado if grade >= passing_grade]  
num_passed = len(passed_students)
total_students = len(grado)  

if total_students > 0:
    passing_percentage = (num_passed / total_students) * 100
    print(f"\nNumber of students Passed: {num_passed} out of {total_students}")
    print(f"Passing percentage: {num_passed}/{total_students} = {passing_percentage:.2f}%")
else:
    print("No grades were entered.")
