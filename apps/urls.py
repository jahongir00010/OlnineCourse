from django.urls import path

from . import course_views
from .views import RegisterView, VerifyEmailView

urlpatterns = [
    path('',  course_views.course_list, name='course_list'),
    path('<slug:slug>/',  course_views.course_detail, name='course_detail'),
path('register/', RegisterView.as_view(), name='register'),
    path('verify/<uid>/<token>/', VerifyEmailView.as_view(), name='verify_email'),
]



