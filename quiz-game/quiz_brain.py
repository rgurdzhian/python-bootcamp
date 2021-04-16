class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    
    def next_question(self):
        q_number = self.question_number + 1
        q_text = self.question_list[self.question_number].text
        user_answer = input(f"Q.{q_number}: {q_text} (True/False)?: ").lower()
        self.check_answer(user_answer, self.question_list[self.question_number].answer.lower())
        self.increase_question_number()
    

    def increase_question_number(self):
        self.question_number += 1


    def all_questions_asked(self):
        return self.question_number == len(self.question_list)


    def check_answer(self, user_answer, correct_answer):
        if (user_answer == correct_answer):
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number + 1}.\n")

    
    def show_final_score(self):
        print("You've completed the quiz!")
        print(f"Your final score is: {self.score}/{self.question_number}")
