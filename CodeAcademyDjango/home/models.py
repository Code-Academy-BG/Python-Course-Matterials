from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=32)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    @classmethod
    def create_person(cls, name, age):
        return cls.objects.create(name=name, age=age)
