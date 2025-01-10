from dotenv import load_dotenv
import os
import sqlite3

connection = sqlite3.connect("example.db") # Connect to db or create if !db
cursor = connection.cursor() # Create cursor object to interact with db


# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    name TEXT NOT NULL,
#     age INTEGER NOT NULL
# )
# """)

# cursor.execute("""
# INSERT INTO users (name, age) VALUES (?, ?)
# """, ("Alice", 25))

load_dotenv() # To protect private or sensitive information

def main():
    print("Main.py action:run")

def learn(x):
    # relevant = n
    # if meTalking = True:
        # listen(me)
            # processInformation()
            # testKnowledge(informationToKeep, oldKnowledge)
                # gatherOwnThoughts(currentKnowledgebase)
                # return informationToKeep
            # grabInsights(informationToKeep)
                # keepOrDiscard(information)
                    # return keep or discard # if statements keep, discard
                    # if keep:
                        # sendToDatabase(information, computer_knowledgebase)                  
            # decideIfRespond(me)
            # decideIfFurtherInvestigate(information)
                # checkRelevance(information)
                # if relevant > #:
                    # sendToDatabase(information, computer_knowledgebase)
                    # furtherInvestigate(sourcesOfInformation)
                # else if relevant < #:
                    # continueListening()
                # else:
                    # continue
    pass

class Computer:
    def __init__(self, parameter):
        self.parameter = parameter

    # Placeholder method for demonstration purposes
    def do_something(self):
        print("computer.do_something() called")

class Me:
    def __init__(self, first_name):
        self.first_name = first_name
    
    # Placeholder method for demonstration purposes
    def learn(self):
        print("me.do_something() called")

class Language:
    def __init__(self, phonology, morphology, syntax, semantics, pragmatics):
        pass
    
    # Placeholder method for demonstration purposes
    def learn(self):
        print("Language.do_something() called")


connection.commit() # Commit changes to the database
connection.close() # Close database connection

if __name__ == "__main__":
    # Computer object
    computer = Computer(
        parameter = "Computer Parameter",
    )

    # Me object
    me = Me(
        first_name = os.getenv("MY_FIRST_NAME")
    )


