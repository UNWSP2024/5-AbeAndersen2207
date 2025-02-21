#UNWSP Programming PythonCos2005DEsp25
#Week#5_Program#1_Kilometer Converter
#02/20/2025
#Abraham. N. Andersen

#Write a program that gives simple math quizzes.  The program should display two random numbers to
# be added, such as     247
#                     + 129
#                     ------
#The program should allow the student to enter the answer.  If the answer is correct, a message of
#congratulations should be displayed.  If the answer is incorrect a message showing the correct answer
#should be displayed.  The program must use a function that accomplishes part of the needed tasks.

# Import the random module to generate random numbers.
import random

# Define a function to display the question and get the answer.
def ask_question(num1, num2):
  """Displays the question and gets the answer from the user.

  Args:
    num1: The first number in the question.
    num2: The second number in the question.

  Returns:
    The answer given by the user.
  """

  # Print the question.
  print(f" {num1:5}")
  print(f"+{num2:5}")
  print("------")

  # Get the answer from the user.
  while True:
      try:
          answer = int(input("Enter your answer: "))
          break
      except ValueError:
          print("Invalid input. Please enter a number.")

  # Return the answer.
  return answer


# Main program loop
while True:
    # Generate two random numbers between 100 and 999.
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)

    # Ask the question and get the answer.
    answer = ask_question(num1, num2)

    # Check the answer.
    correct_answer = num1 + num2
    if answer == correct_answer:
        print("Congratulations! Your answer is correct.")
    else:
        print(f"Sorry, the correct answer is {correct_answer}.")

    # Ask if the user wants to play again.
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
