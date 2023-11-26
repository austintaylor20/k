# Name: Austin Taylor
# D2L Username: atayl220
# Date: 11-26-23

# DO NOT CHANGE THE FILENAME: assignment.py
# The autograder will look for assignment.py. It is also case-sensitive
# So even changing the file name to Assignment.py will score you a zero

### Programming Assignment ###
# Complete the calc_average() and determine_grade() functions
# Compare with the expected result given in the assignment description
# IMPORTANT: Before you submit, make sure your program produces the expected result 
# as shown in the assignment description

# Do NOT change the function header calc_average()
def calc_average():
    # Use a loop and ask the user to enter EIGHT scores
    # Use "Please enter score #{}:".format() to construct the message for input()
    # so that it matches the expected output.
    # DO NOT change the the text, otherwise you may not receive the desired credit




    # convert avg to integer and return the value. Do NOT change
    return int(avg)


# Do NOT change the function header determine_grade(score)
def determine_grade(score):
    # Convert the numeric score into letter grade
    # 90-100:   A
    # 80-89:    B
    # 70-79:    C
    # 60-69:    D
    # below 60: F 


    




    return grade


# Do NOT change any of the lines below
def main():

    avg = calc_average()
    grade = determine_grade(avg)

    print ("Your average grade is:", grade)
score_one = int(input("Enter the first score : "))
score_two = int(input("Enter the second score : "))
score_three = int(input("Enter the third score : "))
score_four = int(input("Enter the fourth score : "))
score_five = int(input("Enter the fifth score : "))
score_six = int(input("Enter the sixth score : "))
score_seven = int(input("Enter the seventh score : "))
score_eight = int(input("Enter the eighth score : "))

def cal_average(first,second,third,fourth,fifth,sixth,seventh,eighth):
    avg = (first + second + third + fourth + fifth + sixth + seventh + eighth / 8)
    return avg

def determine_grade (score) :
    if score < 60:
        grade = "F"

    if score >= 60 and score <= 69:
        grade = "D"
    if score >= 70 and score <= 79:
        grade = "C"
    if score >= 80 and score <= 89:
        grade = "B"
    if score >= 90 and score <= 100:
        grade = "A"

    return grade

print("\nScore \t Grade")
grade = determine_grade (score_one)
print(score_one, "\t", grade)
grade = determine_grade (score_two)
print(score_two, "\t", grade)
grade = determine_grade (score_three)
print(score_three, "\t", grade)
grade = determine_grade (score_four)
print(score_four, "\t" , grade)
grade = determine_grade (score_five)
print(score_five, "\t" , grade)
grade = determine_grade (score_six)
print(score_six, "\t", grade)
grade = determine_grade (score_seven)
print(score_seven, "\t", grade)
grade = determine_grade (score_eight)
print(score_eight, "\t", grade)

average = calc_average(score_one, score_two, score_three, score_four, score_five, score_six, score_seven, score_eight)

print("Average Score: ", average)




main()







if __name__ == "__main__":
    main()
