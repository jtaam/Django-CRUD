from django.contrib import admin
from .models import Project, Category, Expense

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Expense)
