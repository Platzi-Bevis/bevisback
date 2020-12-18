"""Bevis app URLs """

#Django
from django.urls import path

#views
from bevis import views as bevis_views

urlpatterns = [
    path(route='api/v1/course/<int:id_course>/material/<int:id_material>', view=bevis_views.test, name='tests')
]