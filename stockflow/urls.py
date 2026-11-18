from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('', register, name='register'),
    path('login/', loginn, name='loginn'),
    path('logout/', logout_user, name='logout'),
    path('ask-question/', ask_question, name='ask_question'),
    path('answer/',answer_page, name='answer_page'),
    path('create-category/',create_category, name='create_category'),
    path('my-questions/', my_questions, name='my_questions'),
    path('question/<int:id>/', question_detail, name='question_detail'),
    path('question/<int:id>/update/',update_question, name='update_question'),
    path('question/<int:id>/delete/',delete_question, name='delete_question'),
    path('create-answer/<int:id>/',create_answer, name='create_answer'),
    path('create-comment/<int:id>/',create_comment, name='create_comment'),
    path('comments/<int:id>/', view_comments, name='view_comments'),
    path('update-question/<int:id>/',update_question, name='update_question'),
    path('help/', help_page, name='help')
]

