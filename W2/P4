import numpy as np

raw_batch = "   Batch-2026-Computer_Science   "
batch_info = raw_batch.strip()
department_name = batch_info.split("-")[-1].replace("_", " ")

print(f"Batch: {batch_info}")
print(f"Department: {department_name}\n")

subjects = ("Mathematics", "Physics", "Chemistry", "Python", "English")

students = [
    "Alice", "Bob", "Charlie", "David", "Eva", 
    "Frank", "Grace", "Hannah", "Ian", "Jack"
]

print("--- Student Roll Numbers ---")
roll_numbers = list(range(101, 111))
for roll, name in zip(roll_numbers, students):
    print(f"Roll No: {roll} | Name: {name}")
print()


marks = np.array([
    [85, 90, 88, 92, 80],  # Alice
    [70, 75, 65, 80, 72],  # Bob
    [35, 50, 42, 38, 55],  # Charlie (Fails 2 subjects)
    [95, 92, 89, 94, 90],  # David
    [88, 84, 86, 90, 85],  # Eva
    [60, 62, 58, 64, 66],  # Frank
    [45, 38, 50, 40, 48],  # Grace (Fails 1 subject)
    [90, 87, 91, 89, 93],  # Hannah
    [78, 80, 82, 85, 79],  # Ian
    [82, 85, 80, 88, 84]   # Jack
])

total_marks = np.sum(marks, axis=1)
percentages = (total_marks / 500) * 100
subject_averages = np.mean(marks, axis=0)

highest_class_mark = np.max(marks)
lowest_class_mark = np.min(marks)

highest_scoring_student = students[np.argmax(total_marks)]
lowest_scoring_student = students[np.argmin(total_marks)]

class_avg_percentage = np.mean(percentages)

highest_avg_subject = subjects[np.argmax(subject_averages)]
lowest_avg_subject = subjects[np.argmin(subject_averages)]

slicing_sample = marks[0:3, 3:5]

search_subject = "Python"
if search_subject in subjects:
    subj_index = subjects.index(search_subject)
    print(f"Subject '{search_subject}' found at index: {subj_index}\n")

distinction_students = [students[i] for i in range(10) if percentages[i] >= 85]

failed_students = [students[i] for i in range(10) if np.any(marks[i] < 40)]

above_avg_students = [students[i] for i in range(10) if percentages[i] > class_avg_percentage]

reversed_students = list(reversed(students))

alphabetical_students = sorted(students)


print("=" * 50)
print("       ACADEMIC PERFORMANCE SUMMARY REPORT       ")
print("=" * 50)
print(f"Batch Name                  : {batch_info}")
print(f"Department Name             : {department_name}")
print(f"Total Number of Students    : {len(students)}")
print(f"Overall Class Average (%)   : {class_avg_percentage:.2f}%")
print(f"Highest Scoring Student     : {highest_scoring_student}")
print(f"Lowest Scoring Student      : {lowest_scoring_student}")
print(f"Subject with Highest Avg    : {highest_avg_subject} ({np.max(subject_averages):.2f})")
print(f"Subject with Lowest Avg     : {lowest_avg_subject} ({np.min(subject_averages):.2f})")
print(f"Highest Individual Mark     : {highest_class_mark}")
print(f"Lowest Individual Mark      : {lowest_class_mark}")
print(f"Distinction Holders (>=85%) : {len(distinction_students)} {distinction_students}")
print(f"Failed Students (<40 marks) : {len(failed_students)} {failed_students}")
print(f"Students Above Class Avg    : {above_avg_students}")
print("=" * 50)

print("\n--- Slice: First 3 Students, Last 2 Subjects ---")
print(slicing_sample)
