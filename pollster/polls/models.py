from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length = 200) # I.D. initialized automatically as PK, and autoincrement
    publish_date = models.DateTimeField('data published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE) # any deleted question has it's choices also del
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text