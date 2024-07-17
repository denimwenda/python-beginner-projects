import random

def ask_question():
    num_1, num_2, operation, answer = random_problem()
    user_answer = input(f"What is {num_1} {operation} {num_2}? ")
    try:
        user_answer = float(user_answer)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False
    if user_answer == answer:
        print("Correct!")
        return True
    else:
        print(f"Wrong! The correct answer is {answer}.")
        return False

def random_problem():
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    operation = random.choice(["+", "-", "*", "/"])
    
    if operation == "+":
        answer = num_1 + num_2
    elif operation == "-":
        answer = num_1 - num_2
    elif operation == "*":
        answer = num_1 * num_2
    elif operation == "/":
        answer = round(num_1 / num_2, 2)  # rounding to 2 decimal places
    
    return num_1, num_2, operation, answer

def game():
    score = 0
    for _ in range(5):  # ask 5 questions
        if ask_question():
            score += 1
    print(f"Your final score is {score}/5.")

if __name__ == "__main__":
    game()
