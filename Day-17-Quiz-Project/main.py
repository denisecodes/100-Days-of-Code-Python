from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#build question_bank
question_bank = []
for question in question_data:
    q = question["question"]
    a = question["correct_answer"]
    question_bank.append(Question(q, a))

#run quiz
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()



