from django.contrib import admin
from .models import ToDoList, Item, Instruction, ToDoList2, Item2

admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(Instruction)
admin.site.register(ToDoList2)
admin.site.register(Item2)
# Register your models here.
