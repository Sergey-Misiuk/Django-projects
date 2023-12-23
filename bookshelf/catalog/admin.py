from django.contrib import admin

from .models import *



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('first_name','last_name','date_of_birth','date_of_death')
    list_display = ('first_name','last_name','date_of_birth','date_of_death')
    

class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1

 
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','language','image','pdf_file_book','display_genre')
    search_fields = ('title',)
    inlines = [ReviewInline]
    save_on_top = True


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


@admin.register(Reviews)
class CustomReviews(admin.ModelAdmin):
    list_display = ('user','book','content','pub_date')
    
    
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','book')



  
admin.site.register(Language)    

