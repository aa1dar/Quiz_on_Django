from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from typing import List



class QuizResultService():
    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto

    def get_result(self) -> float:

        if(self.quiz_dto.uuid == self.answers_dto.quiz_uuid):
            questions = self.quiz_dto.questions
            answers = self.answers_dto.answers

            n = len(questions)
            score = 0

            answers_dict = dict()

            for answer in answers:
                answers_dict[answer.question_uuid] = answer.choices


            for question in self.quiz_dto.questions:

                question_id = question.uuid
                choices = question.choices
                answer_of_question = answers_dict[question_id]

                ans_len=0

                score_inc = 0
                for choice in choices:
                    if(choice.is_correct):
                        ans_len+=1
                        chid = choice.uuid
                        if(chid in answer_of_question):
                            score_inc+=1

                if(score_inc == ans_len):
                    score+=1

            result = score/n
            result = round(result,2)

            return result
