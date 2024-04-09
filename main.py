#!/bin/python3
#simple python flashcard program
#defines class flash card
import time
import random
import os


class Flashcard:
    def __init__(self):
        self.Questions = {}
        self.Recorded = False
    
    def instruct(self):
        print("Instructions can be found in the Readme.md file")
    
    def extract_Q_and_A(self): #fuction to extract key and value pairs
        mem_file = ""
        self.Questions = dict()
        Q = ""
        A = ""
        try:
            mem_file = open('Memorize.txt', 'r')
        except Exception as e: #error catching
            print("Please create a Memorize.txt file")
            print("Error: " + str(e))
            return False

        for line in mem_file: #iterate over each line
            line = line.strip() #used to remove unnecessary white space
            if not line:
                continue
            if line.startswith("Q:"): 
                self.Recorded = True #variable to make sure a answers come with respective questions
                Q = line[len("Q:"):].strip() #extracts wuestion
            elif line.startswith("A:"):
                if self.Recorded: #condition to make sure  answers come with respective questions
                    A = line[len("A:"):].strip() #extracts answers
                    self.Questions[Q] = A #saves the questions in key and value pairs
                    print(f"Recorded: {Q} - {A}")  
                    self.Recorded = False
                else:
                    print(f"No Question was recorded for this answer: {A}")
        print("Q&A pairs recorded succesfully")
        mem_file.close()
    

    def asking(self): #fuction that asks the questions
     
        if len(self.Questions) == 0: #make sure the dictionnary isn't empty
            print("Couldn't find any Q&A pairs. Please make sure you have them recorded.")
            return
        else: 
            try:
                t = int(input("Enter how long each question should be up for (in seconds): ")) #question display time
                if t <= 0:
                    raise ValueError("Time duration should be a positive integer") 
                question_count = int(input("Enter how many questions you want to ask: ")) #how many questons should be asked
                if question_count <= 0:
                    raise ValueError("Number of questions should be a positive integer.")
                print("Will begin asking questions in 10 seconds. Get ready!")
                time.sleep(10) 
                
                for _ in range(question_count): #iterates over a number of questions
                    question = random.choice(list(self.Questions.keys())) #picks a random question
                    correct_answers = self.Questions[question]
                    print("Question:", question)
                    time.sleep(t) #countdown
                    user_answer = input("\nYour answer: ")
                    if user_answer in correct_answers: #chexks if question is correct
                        print("Your answer is correct!")
                    else:
                        print("Incorrect. The correct answer(s) is/are:", correct_answers)
            except ValueError as e:
                print("Error: Invalid input", e)
            except KeyboardInterrupt:
                print("\nQuestion answering interrupted. Exiting...")

    def exit_program(self):
        exit()

class Menu(Flashcard):
    def __init__(self):
        super().__init__()
        self.options = {
            '1': self.instruct,
            '2': self.extract_Q_and_A,
            '3': self.asking,
            '4': self.exit_program
        }

    
    def execute(self, choice):
        if choice in self.options:
            self.options[choice]()
            input("Press Enter to continue...")
        else:
            print("Invalid option")
    
    def display_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("   FLASHCARD PROGRAM  ")
        print("1. Instuctions")
        print("2. Register Q&A")
        print("3. Run")
        print("4. Exit")


main = Menu()
while True:
    main.display_menu()
    choice = input("Enter your choice: ")
    main.execute(choice)
