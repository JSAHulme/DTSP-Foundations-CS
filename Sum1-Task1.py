import random

#define the function, starting score and number of questions
def run_quiz():
    score = 0
    num_questions = 5

#question loop
#setting the equation variables 
    for question in range(num_questions):
        a = random.randint(1, 10)
        x = random.randint(1, 10)
        b = a * x
        print(f"{a} * x = {b}")
        
        #user input to solve the eqation & check user input is a digit value
        while True:
            user_input = input("Solve the equation. What number is x: ") 
            if user_input.isdigit():
                user_answer = int(user_input)
                break #if answer is a digit break loop and move to line 25
            else:
                print("Invalid input! Please enter a number.")
        
         #check user answer against the x variable, if/else depending on correct or not 
        if user_answer == x:
            print(f"Correct! {a} * {x} = {b}")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {x}.")

#once all 5 questions completed, print total score. 
    print(f"Your total score is {score} out of {num_questions}.")

run_quiz()