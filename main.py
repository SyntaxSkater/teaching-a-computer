from dotenv import load_dotenv
import os

load_dotenv() # To protect private or sensitive information

def main():
    print("Main.py action:run")

def learn(x):
    # oldKnowledge = z
    # relevant = n
    # if meTalking = True:
        # listen(me)
            # processInformation()
            # testKnowledge(informationToKeep, oldKnowledge)
                # gatherOwnThoughts(currentKnowledgebase)
                # return informationToKeep
            # grabInsights(informationToKeep)
                # keepOrDiscard(information)
            # decideIfRespond(me)
            # decideIfFurtherInvestigate(information)
                # checkRelevance(information)
                # if relevant > #:
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

if __name__ == "__main__":
    # Computer object
    computer = Computer(
        parameter = "Computer Parameter",
    )

    # Me object
    me = Me(
        first_name = os.getenv("MY_FIRST_NAME")
    )


