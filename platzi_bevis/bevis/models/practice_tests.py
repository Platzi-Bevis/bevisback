from django.db import models
from .courses import Materials, Courses


class Practice_tests(models.Model):
    title = models.CharField(max_length=100, blank=True)
    case_tests = models.TextField(blank=False)
    description = models.TextField(blank=False)
    boilerplate = models.TextField(blank=False)
    id_material = models.ForeignKey(Materials, on_delete=models.DO_NOTHING)
    id_courses = models.ForeignKey(Courses, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return self.title
