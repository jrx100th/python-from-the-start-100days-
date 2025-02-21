from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

## TODO: Write a for loop to iterate over the question_Data.
## TODO: Create a Question object from each antry in question_data
## TODO: Append each Question object to the question bank

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

# print(question_bank[0].text) --> retreiving data like this
# not like this # print(question_bank[0][text])

# so here the objects till now doesnt have a name
#print(question_bank[0].text, question_bank[0].answer)

while quiz.still_has_questions():
    quiz.next_question()

print("You've copleted the quiz")
print(f"You final score was {quiz.score}/{quiz.question_number}")