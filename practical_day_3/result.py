students = int(input("Students: "))

print("Student\tTotal\tAverage\tGrade")

for i in range(students):

    name = input("Student Name: ")
    marks_input = input("Marks: ").split()

    try:
        marks = []

        for value in marks_input:
            mark = float(value)

            if mark < 0 or mark > 100:
                raise ValueError

            marks.append(mark)

        total = sum(marks)
        average = total / len(marks)

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        print(f"{name}\t{total:.0f}\t{average:.2f}\t{grade}")

    except ValueError:
        print(f"{name}\tInvalid marks")