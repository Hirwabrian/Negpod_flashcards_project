#!/bin/python3
#simple python flashcard program
#defines a class flash card


class flashcard:
    def __innit__(self,textfile,Questions,Recorded):
        self.textfile = textfile
        self.Questions = {}
        self.Recorded = False

    
    def extract_Q_and_A(self):
        try:
            with open(self.textfile, 'r') as f:
                line = f.readlines()
                Q = ""
                A = ""
                for x in line:
                    x = x.strip()
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
    
    
                        

