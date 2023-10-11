students = {
    "8323001": "yzq",
    "8323002": "yqw",
    "8323003": "ljl",
    "8323004": "wjs"
}
to_remove = []
for student_id in students:
    last_digit = int(student_id[-1])
    if last_digit % 2 == 0:
        to_remove.append(student_id)
for student_id in to_remove:
    del students[student_id]

print(students)