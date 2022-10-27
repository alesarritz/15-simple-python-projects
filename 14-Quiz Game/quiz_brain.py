class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        question = self.question_list[self.question_number].text
        answer = input(f"Q.{self.question_number + 1}: {question} (True/False)?: ")
        self.check_answer(answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer):
        if answer.title() == self.question_list[self.question_number].answer:
            self.score += 1
            print("That's right!.")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {self.question_list[self.question_number].answer}")
        print(f"Score: {self.score}/{self.question_number + 1}\n")
        self.question_number += 1

    def completed_quiz(self):
        print("You've completed the quiz.")
        print(f"Final score: {self.score}/{self.question_number + 1}\n")
