import os
import time
import random

Questions = {}  # Define an empty dictionary for storing questions and answers

def instructions():
    print("Instructions can be found in the Readme.md file")
    while True:
        user_input = input("Do you want the instructions to be displayed here? (yes/no): ")
        if user_input.lower() == "yes":
            f = open('README.md', 'r')
            content = f.read()
            print(content)
            f.close()
            break
        elif user_input.lower() == "no":
            print("Exiting...")
            brea
        else:
            print("Invalid input. Please enter yes/no.")
       
def extract_Q_and_A():
    # Function to extract key-value pairs from the file
    global Questions  # Declare Questions as global to modify it inside the function
    mem_file = ""
    Q = ""
    A = ""
    Recorded = False
    try:
        mem_file = open('Memorize.txt', 'r')
    except Exception as e:
        print("Please create a Memorize.txt file")
        print("Error: " + str(e))
        return False

    for line in mem_file:
        line = line.strip()
        if not line:
            continue
        if line.startswith("Q:"):
            Recorded = True
            Q = line[len("Q:"):].strip()
        elif line.startswith("A:"):
            if Recorded:
                A = line[len("A:"):].strip()
                Questions[Q] = A
                print(f"Recorded: {Q} - {A}")
                Recorded = False
            else:
                print(f"There seems to be an error within the text file. Make sure you followed the appropriate syntax")
                return False
    print("Q&A pairs recorded successfully")
    mem_file.close()

def asking():
    if len(Questions) == 0:
        print("Couldn't find any Q&A pairs. Please make sure you have them recorded.")
        return
    else:
        try:
            timer=int(input("Set the questions timer: "))
            if timer <= 0:
                raise ValueError("Number of questions should be a positive integer.")
            question_count = int(input("Enter how many questions you want to ask: "))
            if question_count <= 0:
                raise ValueError("Number of questions should be a positive integer.")

            print("Will begin asking questions in 10 seconds. Get ready!")
            time.sleep(10)

            for _ in range(question_count):
                question = random.choice(list(Questions.keys()))
                correct_answers = Questions[question]  # Accessing Questions directly, no need for self
                print("Question:", question)

                start_time = time.time()
                user_answer = input("\nYour answer: ")
                end_time = time.time()
                elapsed_time = end_time - start_time
                if elapsed_time > timer:
                    print("Time's up! Moving to the next question.")
                    continue
                if user_answer in correct_answers:
                    print("Your answer is correct!")
                else:
                    print("Incorrect. The correct answer(s) is/are:", correct_answers)
        except ValueError as e:
            print("Error: Invalid input", e)
        except KeyboardInterrupt:
            print("\nQuestion answering interrupted. Exiting...")

def exit_program():
    exit()

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("   FLASHCARD PROGRAM  ")
    print("1. Instuctions")
    print("2. Register Q&A")
    print("3. Run")
    print("4. Exit")

# Call the functions

while True:
    display_menu()
    try:
        choice = input("Enter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                instructions()
                input("Press Enter to continue...")
            elif choice == 2:
                extract_Q_and_A()
                input("Press Enter to continue...")
            elif choice == 3:
                asking()
                input("Press Enter to continue...")
            elif choice == 4:
                exit_program()
            else:
                print("Invalid option")
                input("Press Enter to continue...")
        else:
            print("Invalid option. Please enter a number.")
            input("Press Enter to continue...")
    except KeyboardInterrupt:
        print("\nQuestion answering interrupted. Exiting...")
        break
