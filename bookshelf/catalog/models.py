from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, verbose_name='Автор')
    summary = models.TextField(max_length=100, verbose_name='Описание')
    image = models.ImageField(upload_to='images/',verbose_name='Фото',null=True)
    pdf_file_book = models.FileField(upload_to='pdf/',verbose_name='Файл',null=True)
    genre = models.ManyToManyField('Genre', verbose_name='Жанр',related_name='genres_set')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True, verbose_name='Язык')

    class Meta:
        ordering = ['title', 'author']
        
        
        
    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()])

    display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])


    def __str__(self) -> str:
        return self.title



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        
        
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'
    

    def get_absolute_url(self):
        return reverse('author_detail', args=[str(self.id)])




class Genre(models.Model):
    
    LIST_GENRE =(
        ('n','Роман'),
        ('s','История'),
        ('d','Драмма'),
        ('c','Коммедия'),
        ('t','Трагедия'),
        ('p','Поэма'),
        ('f','Фантастика'),
        ('a','Художественная литература'),
        ('l','Лирика'),
        ('w','Обучающие'),
        ('k','Детектив')
        
    )
    
    name = models.CharField(
        max_length=2,
        help_text="Enter a book genre",
        choices=LIST_GENRE,
        unique=True,
        default='b')
    
    
    class Meta:
        ordering = ['-name']

    def __str__(self):
        return f'{self.get_name_display()}'
    
    def get_absolute_url(self):
        return reverse('genre_list', args=[str(self.id)])



class Language(models.Model):
    Language = (
        ('en','English'),
        ('ru','Russia'),
        ('ch','China'),
        ('fr','French'),
        ('po','Portugal'),
        ('ge','Germany'),
        ('sp','Spain')
    )
    
    
    name = models.CharField(
        max_length=50,
        choices=Language,
        unique=True,
        default='en')
    
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.get_name_display()}'



class Reviews(models.Model):
    """Отзывы"""
    book = models.ForeignKey(Book,on_delete=models.CASCADE, verbose_name='книга')
    user = models.ForeignKey(User,verbose_name='пользователь' ,on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Комментарий",max_length=2000)
    pub_date = models.DateField(verbose_name='Дата комментария', auto_now=True)
    
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


    def __str__(self):
        return f"{self.user} - {self.book} - {self.content} - {self.pub_date}"
 



class Profile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, blank=True,on_delete=models.CASCADE, verbose_name='книга')
    
    def __str__(self):
        return str(self.user)


