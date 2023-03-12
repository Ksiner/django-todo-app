from django.db import models
import json

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return json.dumps({ 
            'id': self.id,
            'question_text': self.question_text,
            'pub_date': self.pub_date.isoformat(timespec='milliseconds'),
        })

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return json.dumps({
            'id': self.id,
            'question': self.question,
            'choice_text': self.choice_text,
            'votes': self.votes,
        })