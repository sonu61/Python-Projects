
from day17.question_model import Question
from day17.data import question_data
from day17.quiz_brain import QuizBrain
question_bank=[]
for data in question_data:
    question_text = data["text"]
    question_answer =data['answer']
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
print(question_bank)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

