from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstanse, Language
#
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
#     fields = ['last_name', 'first_name',('date_of_birth', 'date_of_death')]
#
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title','author','display_genre')
#
# @admin.register(BookInstanse)
# class BookInstanseAdmin(admin.ModelAdmin):
#     list_display = ('status','due_back')
#
#     fieldsets = (
#         (None,{
#             'fields':('book','imprint','id')
#
#         }),
#         ('Availability',{
#             'feilds':('status', 'due_back')
#         }),
#     )



admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register (BookInstanse)
admin.site.register (Language)

