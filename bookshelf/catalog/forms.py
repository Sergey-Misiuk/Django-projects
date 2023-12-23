from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from .models import *

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ['title','author','summary','image','pdf_file_book','genre','language']
        
    
    
class ReviewsForm(forms.ModelForm):
    """Форма отзывов"""
        
    content = forms.CharField(max_length=100,  label='Ваш коментарий',widget=forms.Textarea(attrs={'rows': 5}))
    class Meta:
        model = Reviews
        fields = ['content',]



# Добаление книги в профиль

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []




# Поиск по названию

class SerchTitle(forms.ModelForm):
    title = forms.CharField(max_length=100, label='Поиск по названию',widget=forms.TextInput(attrs={'class': 'form-input'}))
    class Meta:
        fields = ['title']
    
   
   
   
   
# Регистрация пользователя 
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='Имя пользователя',widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Введите пароль' ,widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Потвердите пароль',widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
       
       
       
