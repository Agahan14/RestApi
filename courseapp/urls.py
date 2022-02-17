from django.urls import path
from .views import *


urlpatterns = [

    path('category/', CategoryAPIView.as_view()),
    path('category/<int:id>', CategoryDetails.as_view()),
    path('branch/', BranchAPIView.as_view()),
    path('branch/<int:id>', BranchDetails.as_view()),
    path('contact/', ContactAPIView.as_view()),
    path('contact/<int:id>', ContactDetails.as_view()),
    path('course/', CourseAPIView.as_view()),
    path('course/<int:id>', CourseDetails.as_view()),

]