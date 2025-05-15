class QuizBrain:
    def __init__(self,qsn_list):
        self.question_number =0
        self.score=0
        self.question_list=qsn_list
    def still_has_questions(self):
        return len(self.question_list)>self.question_number


    def next_question(self):
        # for qsn in self.question_list:
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer= input(f"{self.question_number}: {current_question.text}.(True/False): ")
        self.check_answer(user_answer,current_question.answer)
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1

        else:
            print(f"you got it wrong.")
        print( f"The correct answer was {correct_answer}")
        print(f"you are right and your score is {self.score}/{self.question_number}")
        print("\n")

