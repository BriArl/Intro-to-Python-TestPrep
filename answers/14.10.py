filename = input().strip()

with open(filename, 'r') as file:
    lines = file.readlines()

students = []
midterm1_total = 0
midterm2_total = 0
final_total = 0
num_students = len(lines)

for line in lines:
    parts = line.strip().split("\t")
    last_name = parts[0]
    first_name = parts[1]
    midterm1 = int(parts[2])
    midterm2 = int(parts[3])
    final = int(parts[4])
    
    avg_score = (midterm1 + midterm2 + final) / 3

    if avg_score >= 90:
        grade = "A"
    elif avg_score >= 80:
        grade = "B"
    elif avg_score >= 70:
        grade = "C"
    elif avg_score >= 60:
        grade = "D"
    else:
        grade = "F"

    students.append((last_name, first_name, midterm1, midterm2, final, grade))

    midterm1_total += midterm1
    midterm2_total += midterm2
    final_total += final

midterm1_avg = midterm1_total / num_students
midterm2_avg = midterm2_total / num_students
final_avg = final_total / num_students

with open("report.txt", 'w') as report:
    for student in students:
        report.write("\t".join(map(str, student)) + "\n")
    
    report.write(f"\nAverages: midterm1 {midterm1_avg:.2f}, midterm2 {midterm2_avg:.2f}, final {final_avg:.2f}\n")
