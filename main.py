#!/bin/python3
# Simple python flashcard program
# Defines a class flash card
import os
import time
import random

class FlashcardProgram:
    def __init__(self):
        self.Questions = {}

    def instructions(self): # method that displays instructions to the user
        print("Instructions can be found in the Readme.md file")
        while True:
            user_input = input("Do you want the instructions to be displayed here? (yes/no): ")
            if user_input.lower() == "yes":
                with open('README.md', 'r') as f:
                    content = f.read()
                    print(content)
                break
            elif user_input.lower() == "no":
                print("Exiting...")
                break
            else:
                print("Invalid input. Please enter yes/no.")

    def  extract_Q_and_A(self):
        try:
            with open('Memorize.txt', 'r') as mem_file:
                Q = ""
                A = ""
                Recorded = False

                for line in mem_file:
                    line = line.strip()
                    if not line:
                        continue
                    if line.startswith("Q:"):
                        if Recorded:
                            # If there was a previously recorded answer without a question,
                            # handle it before moving on to the next question
                            self.Questions[Q] = A
                            print(f"Recorded: {Q} - {A}")
                            A = ""
                        Recorded = True
                        Q = line[len("Q:"):].strip()
                    elif line.startswith("A:"):
                        if Recorded:
                            A = line[len("A:"):].strip()
                        else:
                            print("There seems to be an error within the text file. Make sure you followed the appropriate syntax")
                            return False
            # Handle the last recorded answer if there's no next question
            if Recorded:
                self.Questions[Q] = A
                print(f"Recorded: {Q} - {A}")

            print("Q&A pairs recorded successfully")
        except FileNotFoundError:
            print("Please create a Memorize.txt file")
        except Exception as e:
            print("Error: " + str(e))

    def asking(self): # method that handles the questioning
        if len(self.Questions) == 0:
            print("Couldn't find any Q&A pairs. Please make sure you have them recorded.")
            return
        else:
            try:
                timer = int(input("Set the questions timer: "))
                if timer <= 0:
                    raise ValueError("Timer should be a positive integer.")
                question_count = int(input("Enter how many questions you want to ask: "))
                if question_count <= 0:
                    raise ValueError("Number of questions should be a positive integer.")

                print("Will begin asking questions in 5 seconds. Get ready!")
                time.sleep(5)

                asked_questions = []

                for _ in range(question_count):
                    remaining_questions = set(self.Questions.keys()) - set(asked_questions)
                    if not remaining_questions:
                        print("All questions have been asked. Exiting...")
                        break

                    question = random.choice(list(self.Questions.keys()))
                    correct_answers = self.Questions[question]
                    print("Question:", question)

                    start_time = time.time()
                    user_answer = input("\nYour answer: ")
                    end_time = time.time()
                    elapsed_time = end_time - start_time

                    if elapsed_time > timer:
                        print("Time's up! Moving on.")
                        continue
                    if user_answer in correct_answers:
                        print("Your answer is correct!")
                    else:
                        print("Incorrect. The correct answer(s) is/are:", correct_answers)
                    asked_questions.append(question)
                    print("done")
            except ValueError as e:
                print("Error:", e)
            except KeyboardInterrupt:
                print("\nQuestion answering interrupted. Exiting...")

    def exit_program(self): # method used to exit
        exit()

    def display_menu(self): # method that displays the menu
        os.system('cls' if os.name == 'nt' else 'clear')

        print("   FLASHCARD PROGRAM  ")
        print("1. Instructions")
        print("2. Register Q&A")
        print("3. Run")
        print("4. Exit")

    def run(self): # method used to call the other methods
        while True:
            self.display_menu()
            try:
                choice = input("Enter your choice: ")
                if choice.isdigit():
                    choice = int(choice)
                    if choice == 1:
                        self.instructions()
                        input("Press Enter to continue...")
                    elif choice == 2:
                        self.extract_Q_and_A()
                        input("Press Enter to continue...")
                    elif choice == 3:
                        self.asking()
                        input("Press Enter to continue...")
                    elif choice == 4:
                        self.exit_program()
                    else:
                        print("Invalid option")
                        input("Press Enter to continue...")
                else:
                    print("Invalid option. Please enter a number.")
                    input("Press Enter to continue...")
            except KeyboardInterrupt:
                print("\nQuestion answering interrupted. Exiting...")
                break

if __name__ == "__main__":
    flashcard_program = FlashcardProgram()
    flashcard_program.run()
