from django.shortcuts import render
from .utils import generate_password


def index(request):
    return render(request, 'passgen/index.html')


def password_generator(request):
    
    if request.method == 'POST':
        count_of_letters = int(request.POST.get('letters'))
        count_of_numbers = int(request.POST.get('numbers'))
        count_of_symbols = int(request.POST.get('symbols'))

        password = generate_password(count_of_letters,count_of_numbers,count_of_symbols )

        context = {'password':password}
    return render(request, 'passgen/password.html', context)

        