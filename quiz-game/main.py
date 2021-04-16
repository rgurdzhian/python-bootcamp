from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

questions_bank = []
for question in question_data:
    questions_bank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(questions_bank)

while not quiz.all_questions_asked():
    quiz.next_question()

quiz.show_final_score()