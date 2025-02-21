# question object shoudl have
# text and answer attributes

# new_q = Question("2+3=5","True")

# @constructor
# text = "2+3=5"
# answer = "True"

# TODO 1: Create a Question class with and __init()__ method with two attributes:
# text and answer attribute

class Question:

    def __init__(self,q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


""" testing
new_q = Question("Are you a daffny ?","True")
print(f"Q1. {new_q.text}") # Should call only using what is with the self.
"""
