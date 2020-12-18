"""Bevis app URLs """

#Django
from django.urls import path
from django.urls.resolvers import URLPattern

#views
from bevis import views as bevis_views

urlpatterns = [
    path(route='api/v1/test', view=bevis_views.test, name='tests')
]