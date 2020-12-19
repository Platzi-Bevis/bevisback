from django.contrib import admin

from bevis.models.practice_tests import Practice_tests
from bevis.models.courses import Courses, Materials


@admin.register(Practice_tests)
class Tests(admin.ModelAdmin):
    """Tests practice admin"""

    list_display = (
        "title",
        "case_tests",
        "description",
        "boilerplate",
        "id_material",
        "id_courses",
    )


@admin.register(Courses)
class Courses(admin.ModelAdmin):
    """Courses admin"""


@admin.register(Materials)
class Courses(admin.ModelAdmin):
    """Materials admin"""

