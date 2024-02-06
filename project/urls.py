from django.urls import path
from .views import ListProjectView
urlpatterns=[
    path("list-projects",ListProjectView.as_view(),name='list'),
]