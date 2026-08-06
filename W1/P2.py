marks_list = [54,65,44,57,87,63,91,62,66,76,76]
marks_tuple = tuple(marks_list)

student_name = ["jay","ana","siya","akash","pooja","mahesh","aarav","khushi","kunal","anil","riya"]
student_dict = dict(zip(student_name, marks_list))

highest_marks = max(marks_list)
lowest_marks = min (marks_list)
avrege_marks = sum(marks_list) / len(marks_list)

print(f"Marks_List: {marks_list}")
print(f"Marks Tuple: {marks_tuple}")
print(f"Highest Marks: {highest_marks}")
print(f"Lowesr Marks: {lowest_marks}")
print(f"Avrege Marks: {avrege_marks:.2f}\n")

for name, marks in student_dict.items():
    if mark > avrege_marks:
        print(f"{name}: {marks}")
unique_marks = set(marks_list)
print(f"Unique Marks (Duplicate Removed): {unique_marks}")
