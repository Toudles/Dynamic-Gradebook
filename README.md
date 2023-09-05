Write a gradebook program that lets a teacher keep track of test averages for his or her students. Your program should begin by asking the teacher for a few inputs that will be used to control how the system works. The program should begin by gathering the following information - all of this data must be validated:
  - Number of students in the class: must be positive, no upper limit
  - Number of tests in the class: must be positive, no upper limit
  - Extra credit mode: allows the teacher to enter in scores above 100 points. Valid inputs are "yes" or "no"
  - Drop lowest score mode: allows the system to drop the lowest score for each student. Valid inputs are "yes" or "no". Note: this mode cannot be enabled if the teacher is only         planning on inputting a single test.

Next, prompt the teacher to enter in scores for each student. Ensure that the test score values entered are within the range 0-100 (inclusive on both ends) if "extra credit mode" is turned off. If "extra credit mode" is turned on the upper limit is waived (the score must just be greater than or equal to zero. This data must be validated. 

If "drop lowest score mode" is turned on the system should figure out the lowest score entered for each student, report it to the user and remove it from the grade calculation for the student.

You can assume that the user will enter integers when prompted (but they may not be within the range you are expecting, hence the need for validation)

Once your program has collected all test scores for a student it should display that student's average formatted to 2 decimal places. The program should also compute the student's letter grade using the following chart:
  - A: 90 or above
  - B: [80-90) - inclusive on the lower limit, exclusive on the upper limit
  - C: [70-80) - inclusive on the lower limit, exclusive on the upper limit
  - D: [63-70) - inclusive on the lower limit, exclusive on the upper limit
  - F: [0-63) - inclusive on the lower limit, exclusive on the upper limit

The program should then move onto the next student. When all students have been calculated the program should compute the overall average score for the entire class, along with a count of the letter grades earned by students in the class.
