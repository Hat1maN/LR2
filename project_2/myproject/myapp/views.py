from django.shortcuts import render
from .forms import PasswordForm

def password_view(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            # Здесь можно обработать валидный пароль
            return render(request, 'myapp/success.html')
    else:
        form = PasswordForm()
    return render(request, 'myapp/password_form.html', {'form': form})
    
from django.shortcuts import render

def encyclopedia_view(request):
    # Проверяем cookie темы
    theme = request.COOKIES.get('theme', 'light')  # по умолчанию светлая
    theme_class = 'light-mode' if theme == 'light' else 'dark-mode'
    response = render(request, 'myapp/encyclopedia.html', {'theme': theme_class})
    # Если в cookie нет темы, установим её
    if 'theme' not in request.COOKIES:
        response.set_cookie('theme', 'light')
    return response
