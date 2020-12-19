from django.db import models


class Courses(models.Model):
    title = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title


class Materials(models.Model):
    title = models.CharField(max_length=100, blank=False)
    id_course = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
