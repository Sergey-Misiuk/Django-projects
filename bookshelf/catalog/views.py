from django.shortcuts import render , redirect
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from requests import request

from .forms import *
from .models import *
from django.views.generic import ListView, DetailView
from django.views.generic.base import View


from django.contrib.auth.mixins import LoginRequiredMixin , PermissionRequiredMixin


def index(request):
    """
    Функция отображения домашней страницы
    """
    num_book = Book.objects.all().count()
    num_author = Author.objects.all().count()
    
    
    
    context = {
        'num_book': num_book,
        'num_author': num_author,
    }
    return render(request, 'catalog/index.html', context=context)




# Книги
class BookListView(ListView):
    model = Book
    
    context_object_name = "book_list"
    template_name = "catalog/book_list.html"
    
    paginate_by = 5

    def get_querset(self):
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['genre'] = Genre.objects.all()

        return context



class BookDetailView(FormMixin, DetailView):
    
    
    model = Book
    form_class = ReviewsForm
    template_name = 'catalog/book_detail.html'
    success_url = reverse_lazy('book')
    
    
    
    def get(self, request, *args, **kwargs):
        global current_user
        current_user = request.user
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        prof_obj = Profile.objects.all()
        
        book_db = prof_obj.filter(book_id=self.kwargs.get('pk')).exists()
        user_db = prof_obj.filter(user_id=current_user.id).exists()
        
        book_obj = Book.objects.get(id=self.kwargs.get('pk'))
        
        for profile in prof_obj.filter(user_id=current_user.id):
            if current_user.id == profile.user_id and profile.book_id == book_obj.id:
                if user_db:
                    context['user_db'] = True
                    if book_db:
                        context['book_db'] = True
                        break
            else:
                context['book_db'] = False
                context['user_db'] = False
        return context
   



# Авторы

class AuthorListView(ListView):
    model = Author
    context_object_name = "author_lists"
    paginate_by = 5

    template_name = "catalog/author_list.html"

    def get_querset(self):
        return Author.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context["some data"] = "This if just some data"

        return context


class AuthorDetailView(DetailView):
    model = Author




   
# Создание коментариев для книг
class AddComment(LoginRequiredMixin,View):
    redirect_field_name = ''
    
    def post(self,request,pk):
        form = ReviewsForm(request.POST)
        book = Book.objects.get(id=pk)
        user = request.user
        if form.is_valid():
            form = form.save(commit=False)
            form.book = book
            form.user = user
            form.save()
        return  redirect(book.get_absolute_url())
   
   
# Добавление книг в профиль пользователя

class AddBookProfile(LoginRequiredMixin,View):
    redirect_field_name = ''
    
    def post(self,request,pk):
        forms = ProfileForm(request.POST)
        book = Book.objects.get(id=pk)
        user = request.user
        if forms.is_valid():
            forms = forms.save(commit=False)
            forms.book = book
            forms.user = user
            forms.save()
        return redirect(book.get_absolute_url())
    
    
# Удаление книги  из профиля 

class DeleteBookProfile(LoginRequiredMixin,View):
    redirect_field_name = ''
    
    def post(self,request,pk):
        forms = ProfileForm(request.POST)
        book = Book.objects.get(id=pk)
        user = request.user
        if forms.is_valid():
            for profile in Profile.objects.filter(user_id = user.id):
                if profile.book_id == book.id:
                    Profile.objects.get(id=profile.id).delete()
        return  redirect(book.get_absolute_url())
   
   
# Редактирование книг  
class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')
    
    
    def post(self,request):
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print('ФОРМА НЕ ВАЛИДНА')
        return  redirect('index')
    def get_success_url(self):
        return reverse('')
    
    
class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('book')
    
    
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book')   
   
   
   
   
#  Авторы

# Редактирование авторов 
class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    
class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'
    
class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('book')   



from django.dispatch import receiver
from django.contrib.auth.models import Group, User
from django.dispatch import Signal



# Регистрация пользователя 



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Регистрация' 
        return context
    
    
    



# Профиль пользователя

def ProfileUser(request):
    book = Profile.objects.filter(user_id=request.user.id)
    context = {
        'book':book,
    }
    return render(request, 'catalog/profile.html',context=context)



class FilterBook(ListView):
    model = Genre
    
    def get_queryset(self):
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gr = Genre.objects.get(id=self.kwargs['pk'])
        context['genre'] = Genre.objects.all()
        context['genre_name'] = gr
        context["book_list"] = gr.genres_set.all
        
        
        return context
    
    


class Search(ListView):
    
    paginate_by = 5
        
    def get_queryset(self):
        return Book.objects.filter(title__iregex=self.request.GET.get('q'))
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get('q')
        context['genre'] = Genre.objects.all()
        return context
        
    
    
