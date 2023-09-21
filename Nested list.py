python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

unique_scores = set()
repeated_names = []

for student in python_students:
    name = student[0]
    score = student[1]
    
    if score in unique_scores:
        repeated_names.append(name)
    else:
        unique_scores.add(score)

for name in repeated_names:
    print(name)