"""
Assignment #5, Part 2
Andrew Park
"""

students = int(input("How many students are in your class? "))
while students < 0:
    print("Invalid # of students, try again.")
    students = int(input("How many students are in your class? "))
print()
tests = int(input("How many tests will you be giving in this class? "))
while tests < 0:
    print("Invalid # of tests, try again.")
    tests = int(input("How many tests will you be giving in this class? "))
print()
while True:
    ec = input("Is extra credit allowed? This will permit test scores to exceed 100 points (yes/no): ").upper()
    if ec == "YES":
        break
    elif ec == "NO":
        break
    else:
        print("Invalid choice try again")
print()

if tests == 1:
    print("Drop lowest test score mode turned off (only 1 test being entered)")
    drop = "NO"
else:
    while True:
        drop = input("Would you like to drop the lowest test for each student? (yes/no): ").upper()
        if drop == "YES":
            break
        elif drop == "NO":
            break
        else:
            print("Invalid choice, try again.")

print()

print("Thanks, here we go!")
print()

total = 0
A = 0
B = 0
C = 0
D = 0
F = 0

for i in range(1, students + 1):

    print("*** Student #",i,"***")
    score = 0
    x = 9999999999999999999999999999999999999
    for t in range(1, tests + 1):
        if ec == "NO":
            while True:
                t1 = int(input("Enter score for test #" + str(t) + ": "))
                if t1 > 100:
                    print("Extra credit mode is not enabled. Try again")
                elif t1 < 0:
                    print("Score cannot be negative. Try again")
                else:
                    score += t1
                    if t1 < x:
                        x = t1
                    break
        else:
            while True:
                t1 = int(input("Enter score for test #" + str(t) + ": "))
                if t1 < 0:
                    print("Score cannot be negative. Try again")
                else:
                    score += t1
                    if t1 < x:
                        x = t1
                    else:
                        t1 = x
                    break

    if drop == "YES":
        print()
        score -= x
        t2 = format(x, ".1f")
        print("Dropping the lowest test score for this student", " (",(t2),")",sep="")
        average1 = (score / (tests-1)) 
        avg = format(average1, ".2f")
        total += float(avg)
        total1 = (total / students)
        total2 = format(total1, ".2f")
    else:
        print()
        average1 = (score / tests) 
        avg = format(average1, ".2f")
        total += float(avg)
        total1 = (total / students)
        total2 = format(total1, ".2f")
    if float(avg) >= 90:
        grade = "(A)"
        A += 1
    elif 80 <= float(avg) < 90:
        grade = "(B)"
        B += 1
    elif 70 <= float(avg) < 80:
        grade = "(C)"
        C += 1
    elif 63 <= float(avg) < 70:
        grade = "(D)"
        D += 1
    elif 0 <= float(avg) < 63:
        grade = "(F)"
        F += 1
    
    if float(total2) >= 90:
        grade1 = "(A)"
    elif 80 <= float(total2) < 90:
        grade1 = "(B)"
    elif 70 <= float(total2) < 80:
        grade1 = "(C)"
    elif 63 <= float(total2) < 70:
        grade1 = "(D)"
    elif 0 <= float(total2) < 63:
        grade1 = "(F)"
    print("Average score for student #",i,"is", avg, grade)
    print()
print("----- REPORT -----")
print("Overall class average: ", total2, grade1)
print("# of students who earned an 'A' average: ", A)
print("# of students who earned an 'B' average: ", B)
print("# of students who earned an 'C' average: ", C)
print("# of students who earned an 'D' average: ", D)
print("# of students who earned an 'F' average: ", F)


