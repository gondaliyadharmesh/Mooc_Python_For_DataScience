Roll_No = 250160450310
Name = "Dharmesh Gondaliya"
Age = 22
Student_Marks = [
    {"Subject": "Cyber", "Volume": 60},
    {"Subject": "Big_Data", "Volume": 75},
    {"Subject": "Python", "Volume": 85}
    ]

total_marks = sum(item["Volume"] for item in Student_Marks)
total_subject = len(Student_Marks)
Max_Marks = total_subject * 100
percentage = (total_marks / Max_Marks) * 100

print("=" * 40)
print(f"Roll No: {Roll_No}")
print(f"Name: {Name}")
print(f"Age: {Age}")
print("=" * 40)
print("Subject Mark")
for Subject in Student_Marks:
    print(f" -{Subject['Subject']}, {Subject['Volume']}")

print("=" * 40)
print(f"total_marks: {total_marks} / {Max_Marks}")
print(f"percentage  : {percentage:.2f}%")
print("=" * 40)
