from django.db import models

class Question(models.Model):
    """
    Represents a poll question.

    Fields:
        question_text (CharField): The text of the question.
        pub_date (DateTimeField): The date and time the question was published.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        Returns the string representation of the question.
        """
        return str(self.question_text)


class Choice(models.Model):
    """
    Represents a choice for a specific poll question.

    Fields:
        question (ForeignKey): The related Question object.
        choice_text (CharField): The text of the choice.
        votes (IntegerField): The number of votes this choice has received.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        Returns the string representation of the choice.
        """
        return str(self.choice_text)
