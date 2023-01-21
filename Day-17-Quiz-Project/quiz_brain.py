#TODO: asking the questions

class QuizBrain:
    #give attributes to the question list with question number
    def __init__(self, question_list):
        self.question_num = 0
        self.score = 0
        self.question_list = question_list

# TODO: checking if we're the end of the quiz
    def still_has_question(self):
        if self.question_num < len(self.question_list):
            return True
        else:
            print("You've completed the quiz")
            print(f"Your final score was: {self.score}/{self.question_num}")
            return False

    #displays next question by retrieving from question list
    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

#TODO: checking if the answe was correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your curent score is {self.score}/{self.question_num}")
        print("\n")


