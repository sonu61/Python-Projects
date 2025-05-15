# class User:
#     def __init__(self,user_id,user_name):
#         print('new user being created...')
#         self.user_id=user_id
#         self.user_name = user_name
#         self.followers =0
#         self.following=0
#
#     def follow(self,user):
#         user.followers+=1
#         self.following+=1
#
#
#
# user_1=User('12','Sonu')
# user_2=User('11','samit')
# user_2.follow(user_1)
#
# print(user_1.followers)
# print(user_1.following)
#
#
# print(user_2.followers)
# print(user_2.following)
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

