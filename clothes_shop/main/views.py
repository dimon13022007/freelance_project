from django.shortcuts import render, redirect

from .models import User
from .models import Article


from django.contrib.auth import logout

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def regist(request):

    # Массив для передачи данных шаблону
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        form = UserCreationForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            user = form.save()
            # Хеширование пароля
            user.set_password(form.cleaned_data.get('password1'))
            user.save()

            login(request, user)
            # Получение данных из формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            confirm_password = form.cleaned_data['password2']

            # Создание объекта User и сохранение его в базе данных
            user = User.objects.create(username=username, password=password, confirm_password=confirm_password)

            data['username'] = username
            # Передача формы к рендеру
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"
            next_url = request.POST.get('next', '/')
            return redirect(next_url)
            # Рендеринг страницы

    else:  # Иначе
        # Создаём форму
        form = UserCreationForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендеринг страницы
        return render(request, 'main/registr.html', data)


def index(request):
    return render(request, 'main/index.html')





def check(request):
    last_user = User.objects.last()  # Получаем последнего пользователя из базы данных
    users = [last_user]  # Создаем список, содержащий только последнего пользователя
    context = {'users': users}  # Создаем контекст шаблона, содержащий пользователей
    return render(request, 'main/check.html', context)


def advertisement(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        intro = request.POST.get('intro')
        text = request.POST.get('text')
        article = Article(title=title, intro=intro, text=text)
        article.save()
        return redirect('/')

    else:
        ads = Article.objects.all()
        return render(request, 'main/advertisement.html', {'ads': ads})


def posts(request):
    articles = Article.objects.all().order_by('text')
    return render(request, 'main/posts.html', {'articles': articles})






def payment_view(request):
    return render(request, 'main/payment.html')



def payment_successful(request):
    return render(request, 'main/payment2.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def contacts(request):
    return render(request, 'main/contacts.html')