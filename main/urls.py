from django.urls import path
from . import views # imports the views with the webpages from the directory



urlpatterns = [path("", views.index, name = "index"),
               path("goodbye", views.goodbye, name = "goodbye"),
               #path("<int:id>", views.index3, name = "index3"), # it doesn't seem to matter if I chose index1 or index2
               #path("<str:name>", views.index2, name = "index2"), this does not need to pointed to by economicsmodel.urls.py
               path("home", views.home, name="home"),
               #path("<str:name>", views.index3, name = "index3"),
               path("create/", views.create, name = "create"),
               path("list", views.list, name = "list"),
               path("todo", views.todo,name = "todo"),
               path("add_item", views.add_item, name = 'Add_item'),
               path("todo2", views.todo2,name = "todo2"),
               path('<int:todolist2_id>/todo/',views.todosum,name='summary'),
               path("todo2index",views.todo2index, name = "ToDo2Index"),
               path('<int:name_id>/', views.detail, name='detail'),
               ]