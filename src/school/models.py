from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)


class Student(models.Model):
    firstname = models.CharField(max_length=50),
    lastname = models.CharField(max_length=50)
    group = models.ForeignKey(
        Group,
        null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='students'
    )

    def __str__(self):
        return f'{self.lastname}'


class Diary(models.Model):
    avg_score = models.DecimalField(max_digits=3, decimal_places=2)
    student = models.OneToOneField(Student, null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name='diary')

    def __str__(self):
        return f"diary_id - {self.id}, student's name - {self.student.firstname}"


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    pages = models.CharField(max_length=10000)
    student = models.ManyToManyField(Student, related_name='books', null=True, blank=True)

