from django.db import models

# Create your models here.

#Each class is represented by a class that subclasses django.db.models.Model
#each model , # of class variables , database field
#field - instance of Field class: e.g. CharField.
#Note that: relationship is defined using ForeignKey : it tells Django that each choice is related to a single Question.


class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        Its important to add str methods not only for our convenience, but also due to the fact
        that object representations are used throught auto generated admin.
        """
        return self.question_text


class Choice(models.Model):
    """
    question is connected to Question class.
    can be used as:
    q.choice_set.create(choice_text = "Not much",votes = 0)
    q.choice_set.create(choice_text= "The sky",votes = 0)
    to see all choice:
    q.choice_set.all()
    #note that q is a Question object.
    """
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        """
        Its important to add str methods not only for our convenience, but also due to the fact
        that object representations are used throught auto generated admin.
        """
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
