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
