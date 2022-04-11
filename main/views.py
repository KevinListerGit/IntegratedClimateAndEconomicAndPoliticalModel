from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList, Item, Instruction, ToDoList2, Item2
from .forms import CreateNewList
from .forms import ItemForm
from django.template import loader


# Create your views here.
def index(response):
    return HttpResponse("Hello world")

def goodbye(response):

    return HttpResponse("<h1>Goodbye world,</h1>")

def index1(response,id):
    ls = ToDoList.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" % ls.name)   # % used for string manipulation https://www.geeksforgeeks.org/what-does-s-mean-in-a-python-format-string/#:~:text=%25s%20specifically%20is%20used%20to,conversion%20from%20value%20to%20string.

def index2(response,name):
    ls = ToDoList.objects.get(name=name)
    item = ls.item_set.get(id=1) #id refers to the items list.
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % (ls.name, str(item.text)))   # % used for string manipulation https://www.geeksforgeeks.org/what-does-s-mean-in-a-python-format-string/#:~:text=%25s%20specifically%20is%20used%20to,conversion%20from%20value%20to%20string.

def index3(response,id):  # the id needs to be the same as the variable in the urls statement that call this function
    ls = ToDoList.objects.get(id=id)
    #return render(response, "main/base.html", {"name":ls.name}) previous version to display on the name on the page
    return render(response, "main/viewitems.html", {"ls": ls}) # sets ls to the entire data set.

def home(response):
    return render(response, "main/home.html", {"name":"there is no list on the home page"})

def create(response):
    #form = CreateNewList()
    #return render(response, "main/create.html", {"form":form})
    print("say hello postie before If")
    print("response method is", response.method)
    #if response.method == 'POST':

    if response.method == 'POST':
        print("say hello postie after IF")
        form_1 = CreateNewList(response)  #response.Post obtains the data from the form

        if form_1.is_valid == True: #checks if all fields are completed in form
            n = form_1.cleaned_data["Name"] #cleaned_data unencrypts the data. name is populated from forms.Creatlist
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%t" %t.id)
        #return HttpResponseRedirect("/1")
        # return HttpResponse("<h1>Goodbye world,</h1>")
    else:
        form=CreateNewList()
    return render(response, "main/create.html", {"form": form})


#def index1(response,id):
#    return HttpResponse("<h1>%s</h1>" % id)   # % used for string manipulation https://www.geeksforgeeks.org/what-does-s-mean-in-a-python-format-string/#:~:text=%25s%20specifically%20is%20used%20to,conversion%20from%20value%20to%20string.

def list(request):


    ls = Item.objects.all()
    #template = loader.get_template("main/list.html",{"name".ls.name})
    #ItemList = Item.objects.all()
    #print ("ls", ls)

    #return render(request, 'main/list.html', {"ls":ls, "ItemList":ItemList})
    return render(request, 'main/list2.html', {"ls": ls})

def todo(request):
    todolist = ToDoList.objects.all
    ls = Item.objects.all()
    return render(request, "main/todo.html", {"todo": todolist, "ls": ls})

def add_item(request):
    submitted = False
    if request.method == "POST":

        form = ItemForm(request.POST)
        if form.is_valid():
            TextFromForm = form.cleaned_data['text']
            print ("ready to save", TextFromForm)
            form.save()
            return HttpResponseRedirect('/add_item?submitted=True')
    else:
        form = ItemForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "main/Add_item.html", {'form': form, 'submitted': submitted})

def todo2(request):
    todolist2 = ToDoList2.objects.all
    ls = Item.objects.all()
    return render(request, "main/todo2.html", {"todo2": todolist2, "ls": ls})

def index(request):
    latest_question_list = ToDoList2.objects.order_by('name')[:2]
    output = ', '.join([q.name for q in latest_question_list])
    return HttpResponse(output)

def todosum(request, todolist2_id):
    t = ToDoList2.objects.get(id=todolist2_id)
    s = str(todolist2_id)
    #print ("string =", s)
    #print (t)
    #AddStrings = s+t

    #string = t + " " + str(todolist2_id)
    #print (string)
    return HttpResponse('Todolist %s' %todolist2_id)

def todo2index(request):
    latest_todo_list = ToDoList2.objects.order_by('name')
    #output =", ".join([q.name for q in latest_todo_list])
    #return HttpResponse(output)
    template = loader.get_template('main/indextodo.html')
    context = {'latest_todo_list':latest_todo_list}
    return HttpResponse(template.render(context,request))

def detail(request, name_id):
    try:
        todolist = ToDoList2.objects.get(pk=name_id)
        itemlist = Item2.objects.filter(todolist2_id=name_id)
        print(Item2.objects.filter(todolist2_id=name_id))
    except ToDoList2.DoesNotExist:
        raise Http404("No todo list exists")
    return render(request, 'main/detail.html',{'todolist':todolist, 'itemlist':itemlist})