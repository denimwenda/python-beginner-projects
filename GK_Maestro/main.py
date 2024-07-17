"""
This game test our general knowledge skills!
You just need to answer the 10 questions correctly to become the winner!
"""

from question_bank import *
from answer_bank import *
from random import randint, choice
from art import *

# Main functionality
def main():
    # Counter for questions
    ques_count = 1
    
    # Store the score
    score = 0
    
    # Loop until 10 questions are asked
    while ques_count <= 10:
        # Store question number and the question
        question_tuple = generate_question()
        
        # Store the question
        question = question_tuple[1]
        
        # Display the question on the screen
        print(f"Question No. {ques_count}: {question}")
        
        # Increase question count by 1
        ques_count += 1
        
        # Record user answer
        user_answer = input("Answer: ")
        
        # Generate and store the correct answer
        correct_answer = generate_answer(question_tuple[0])
        
        # Update score by 1 if the answer matches, and display the score
        if user_answer.lower() == correct_answer.lower():
            score += 1
            print(f"Correct Answer. Your Score: {score}")
            # Alert about wrong answer, and display the score
        else:
            print(f"Wrong Answer. Your Score: {score}")
        
    # Display final score on the screen
    if score == 10:
        print("Congratulations!")
        print("You have answered all 10 questions correctly!")
        
# Generate question for the user
def generate_question():
    # List the question numbers and their difficulty level
    easy_qlist = [2, 3, 4, 8, 9, 14, 15, 16]
    hard_qlist = [1, 5, 6, 7, 10, 11, 12, 13]
    
    # Choose a random value - 1 or 2
    difficulty = randint(1, 2)
    
    # Difficulty level: easy
    if difficulty == 1:
        # Select a random question from the choices
        random_choice = choice(easy_qlist)
        ques = easy_question(random_choice)
    # Difficulty level: hard
    elif difficulty == 2:
        # Select a random question from the choices
        random_choice = choice(hard_qlist)
        ques = hard_question(random_choice)
        
    # Return question number and the answer
    return random_choice, ques

# Generate and macth the answer of the user
def generate_answer(num):
    actual_answer = answer(num)
    return actual_answer

# When the program is run, main function is called
if __name__ == "__main__":
    main()