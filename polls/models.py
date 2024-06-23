from datetime import datetime

from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def vote(self):
        self.votes += 1
        self.save()


class ChoiceRate(models.Model):
    choice_rate = models.IntegerField(default=1)


class Student(models.Model):
    name = models.CharField(max_length=70)


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    students = models.ManyToManyField(Student,through='Enrollment')


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enroll_date = models.DateTimeField(auto_now=True)