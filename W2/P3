Total_Student = 10
Num_Subject = 5
Pass_Marks = 40

students = [
    {"roll": 1, "name": "jay", "marks": (56, 45, 76, 77, 51)},
    {"roll": 2, "name": "vishal", "marks": (44, 64, 76, 75, 87)},
    {"roll": 3, "name": "priya", "marks": (65, 76, 86, 56, 88)},
    {"roll": 4, "name": "aman", "marks": (55, 43, 61, 39, 72)},
    {"roll": 5, "name": "janak", "marks": (44, 64, 76, 75, 87)},
    {"roll": 6, "name": "amisha", "marks": (60, 65, 70, 75, 80)},
    {"roll": 7, "name": "maya", "marks": (88, 91, 85, 89, 94)},
    {"roll": 8, "name": "paresh", "marks": (35, 30, 45, 50, 40)},
    {"roll": 9, "name": "naresh", "marks": (78, 82, 80, 85, 87)},
    {"roll": 10, "name": "nayan", "marks": (92, 88, 94, 90, 91)},
]


def get_grade(percentage):
    if percentage >= 85:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 55:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


for student in students:
    total = sum(student["marks"])
    percentage = total / Num_Subject
    grade = get_grade(percentage)

    student["total"] = total
    student["percentage"] = percentage
    student["grade"] = grade

class_avg_percentage = sum(s["percentage"] for s in students) / len(students)

max_percentage = max(s["percentage"] for s in students)
min_percentage = min(s["percentage"] for s in students)

highest_scorers = [
    s["name"] for s in students if s["percentage"] == max_percentage
]
lowest_scorers = [
    s["name"] for s in students if s["percentage"] == min_percentage
]

above_avg_students = [
    s["name"] for s in students if s["percentage"] > class_avg_percentage
]

failed_students = [
    s["name"] for s in students if any(mark < Pass_Marks for mark in s["marks"])
]

grade_dict = {"A": [], "B": [], "C": [], "D": [], "F": []}
for student in students:
    grade_dict[student["grade"]].append(student["name"])

first_max = -1
second_max = -1

for student in students:
    p = student["percentage"]
    if p > first_max:
        second_max = first_max
        first_max = p
    elif p > second_max and p != first_max:
        second_max = p

second_highest_scorers = [
    s["name"] for s in students if s["percentage"] == second_max
]

subject_averages = []
# Fixed: Num_Subject (singular)
for sub_idx in range(Num_Subject):
    sub_total = sum(student["marks"][sub_idx] for student in students)
    subject_averages.append(sub_total / len(students))

best_subject_idx = subject_averages.index(max(subject_averages)) + 1

seen_names = set()
duplicates = set() 

for student in students:
    name = student["name"]
    if name in seen_names:
        duplicates.add(name)
    else:
        seen_names.add(name)

unique_students = list(seen_names)

print("=" * 50)
print("       STUDENT PERFORMANCE ANALYTICS REPORT       ")
print("=" * 50)

print(f"\nClass Average Percentage: {class_avg_percentage:.2f}%")
print(
    f"Highest Scorer(s) ({max_percentage:.2f}%): {', '.join(highest_scorers)}"
)
print(f"Lowest Scorer(s) ({min_percentage:.2f}%): {', '.join(lowest_scorers)}")

print("\nStudents Scoring Above Class Average:")
print(", ".join(above_avg_students))

print("\nStudents Failing in 1 or More Subjects:")
print(", ".join(failed_students) if failed_students else "None")

print("\nStudents Grouped by Grade:")
for grade, names in grade_dict.items():
    print(f"  Grade {grade}: {', '.join(names) if names else 'None'}")

print("\nStudents in Alphabetical Order (Original Data Untouched):")
alphabetical_names = sorted([student["name"] for student in students])
print(", ".join(alphabetical_names))

print(f"\nSecond Highest Scorer(s) ({second_max:.2f}%):")
print(", ".join(second_highest_scorers))

print(f"\nSubject with Highest Class Average:")
print(
    f"  Subject {best_subject_idx} with average mark: {max(subject_averages):.2f}"
)

print("\nDuplicate Student Names Check:")
if duplicates:
    print(f"  Duplicate entries found: {', '.join(duplicates)}")
else:
    print("  No duplicate student names found.")

print("\nUnique Student Names Count:", len(unique_students))
print("=" * 50)
