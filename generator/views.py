from django.shortcuts import render
from django.http import HttpResponse
import random

def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')



def password(request):
    
    characters = list('abcdefghijklmnñopqrstuwxyz')
    generated_password=''
    length=int(request.GET.get('length')) 
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
        
    
    for i in range(length):
        
        generated_password+=random.choice(characters)
        
    
    return render(request, 'password.html',{'password':generated_password})