result = {}

for i in range(5):
    score = int(input(f"Enter score {i+1}: "))
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    if grade in result:
        result[grade] += 1
    else:
        result[grade] = 1

for grade, count in result.items():
    print(f"{grade}: {count}")


