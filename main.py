#!/bin/python3
#simple python flashcard program
#defines a class flash card
import time
import random


class Flashcard:
    def __init__(self):
        self.Questions = {}
        self.Recorded = False
    
    def instruct(self):
        print("Instructions can be found in the Readme.md file")
    
    def extract_Q_and_A(self,textfile =""):
        textfile = input("input the text file name:  ")
        self.textfile = textfile
        try:
            with open(self.textfile, 'r') as f:
                line = f.readlines()
                Q = ""
                A = ""
                for x in line:
                    x = x.strip()
                    if not x:
                        continue
                    if x.startswith("Q:"):
                        self.Recorded = True
                        Q = x[len("Q:")].strip()
                        self.Questions[Q] = []
                    elif x.startswith("A:"):
                        if self.Recorded:
                            A = x[len("A:")].strip()
                            self.Questions[Q].append(A)
                            self.Recorded = False
                        else:
                            print("No Question was recorded for this answer")
        except FileNotFoundError:
            print(f" file {self.textfile} not found")
    
    def asking(self,count,t):
        count=0
        t = int(input("Enter how long the questions should be up for(in seconds)"))
        print("will begin asking Questions in 10 seconds get ready!!")
        if not self.Questions:
            return ("Couldnt find any Q&A please make sure you had them recorded.")
        time.sleep(10)

        for count in range(5):
            question = random.choice(list(self.Questions.keys()))
            correct_answer = self.Questions[question]
            while t > 0:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print("Questions:", question)
                print(timer, end="\r")
                time.sleep(1) 
                t -= 1
                user_asnwer = input("Your anwer: ")
                if user_asnwer in correct_answer:
                    print("Your answer is correct")
                else:
                    print("Incorrect. the correct answer is,", correct_answer)
            count =+ 1
        
    def exit_program(self):
        exit

class Menu(Flashcard):
    def __init__(self):
        self.options = {
            '1': self.instruct,
            '2': self.extract_Q_and_A,
            '3': self.asking,
            '4': self.exit_program
        }
    
    def execute(self, choice):
        if choice in self.options:
            self.options[choice]()
        else:
            print("Invalid option")
    
    def display_menu(self):
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

        

  


        
            
        


    
    
                        

