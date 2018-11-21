from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=50)
    closed = models.BooleanField(False)
    pub_date = models.DateField()

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text =  models.CharField(max_length=100)
    votes = models.IntegerField()
    question = models.ForeignKey(Question,on_delete = models.CASCADE, related_name = "choices")
    def __str__(self):
        return self.choice_text