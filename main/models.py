from django.db import models

class Questions(models.Model):
    question = models.TextField('Question')

    answer1 = models.CharField('answer1', max_length=250,default='')
    answer2 = models.CharField('answer2', max_length=250,default='')
    answer3 = models.CharField('answer3', max_length=250,default='')
    answer4 = models.CharField('answer4', max_length=250,default='')

    true_answer = models.CharField('True Answer', max_length=250,default='')

    user_answer = models.TextField('User Answer', max_length=250,default='-')

    def __str__(self):
        return self.question


