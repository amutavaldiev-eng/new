from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import *

def register(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        if username and password:
            User.objects.create_user(
                username = username,
                password = password
            )
        return redirect('loginn')
    return render(request,'registration.html')

def loginn(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(
            request,
            username=data.get('username'),
            password=data.get('password')
        )
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')
    
@login_required
def logout_user(request):
    logout(request)
    return redirect('loginn')

def home(request):
    questions = Question.objects.all()
    return render(request, 'home.html', {'questions': questions})


@login_required
def create_category(request):
    if request.method == 'POST':
        Category.objects.create(name=request.POST.get('name'))
        return redirect('home')
    return render(request, 'create_category.html')



@login_required
def ask_question(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        Question.objects.create(
            user=request.user,
            category_id=request.POST.get('category'),
            title=request.POST.get('title'),
            desc_ques=request.POST.get('desc_ques')
        )
        return redirect('home')
    return render(request, 'ask_question.html',{'categories': categories})




@login_required
def update_question(request, id):
    question = Question.objects.get(pk=id, user=request.user)
    categories = Category.objects.all()
    if request.method == 'POST':
        question.title = request.POST.get('title')
        question.desc_ques = request.POST.get('desc_ques')
        question.category_id = request.POST.get('category')
        question.save()
        return redirect('question_detail', id=question.id)
    return render(request, 'update_question.html', {'question': question,'categories': categories})



@login_required
def delete_question(request, id):
    question = Question.objects.get(id=id, user=request.user)
    if request.method == 'POST':
        question.delete()
        return redirect('home')
    return render(request, 'delete_question.html', {'question': question})



@login_required
def my_questions(request):
    questions = Question.objects.filter(user=request.user)
    return render(request, 'my_questions.html', {'questions': questions })



@login_required
def create_answer(request, id):
    question = Question.objects.get(pk=id)
    if request.method == 'POST':
        Answer.objects.create(
            question=question,
            user=request.user,
            body=request.POST.get('body'))
        return redirect('question_detail', id=question.id)
    return render(request, 'create_answer.html',{'question': question })


def answer_page(request):
    categories = Category.objects.all()
    questions = Question.objects.all()
    questions = Question.objects.exclude(user=request.user)
    cat = request.GET.getlist('category')
    search = request.GET.get('q')
    if cat:
        questions = questions.filter(category__id__in=cat)

    if search:
        questions = questions.filter(Q(title__icontains=search))
    return render(request, 'answer.html', {'categories': categories,'questions': questions,'checked_cat': list(map(int, cat)),'query': search})




def question_detail(request, id):
    question = Question.objects.get(pk=id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'question_detail.html', {'question': question,'answers': answers})

@login_required
def create_comment(request, id):
    answer = Answer.objects.get(pk=id)
    if request.method == 'POST':
        Comment.objects.create(
            answer=answer,
            user=request.user,
            body=request.POST.get('body')
        )
        return redirect('question_detail', id=answer.question.id)
def view_comments(request, id):
    question = Question.objects.get(id=id)
    answers = Answer.objects.filter(question=question)
    comments = Comment.objects.filter(answer__in=answers)
    return render(request, 'comments.html', {
        'question': question,
        'comments': comments
    })
 
def help_page(request):
    return render(request, 'help.html')