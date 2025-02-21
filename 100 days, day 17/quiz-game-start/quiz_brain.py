# TODO: Checking the user for the next question

# TODO: Checking if the answer was right

# TODO: Checking if were at the end of the quiz

# TODO: This class has two attributes question_number = 0,question_list
# TODO: method --> next_question



# TODO: Create a class called QuizBrain,
# TODO: Write an __init__() method, initialize the question number to 0
# TODO: Initialize the question_list to an input

class QuizBrain:

    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # create a method called the next question
    # should retrieve the item at the current question number
    # from the question_list
    # Use the input() function to show the user the question text and ask for the users answer
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number} : {current_question.text}(True/False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer is : {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")