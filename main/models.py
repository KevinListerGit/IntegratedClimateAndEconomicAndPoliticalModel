from django.db import models

# Create your models here.



class ToDoList(models.Model):

    name = models.CharField('To Do List name', max_length=200)
    #item = models.CharField ('Item')
    #item = models.ForeignKey(Item,blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Instruction(models.Model):

    InstructionText= models.CharField(max_length=100)

    def __str__(self):
        return self.InstructionText

class Item(models.Model):

    text = models.CharField(max_length=300)
    complete = models.BooleanField(blank=True,null=True) #this blank and null must be set or the files will not be saved
    ToDoList = models.ForeignKey(ToDoList, blank=True, null=True, on_delete=models.CASCADE)
    InstructionDetail = models.ManyToManyField(Instruction,blank=True)

    def __str__(self):
        return self.text




class ToDoList2(models.Model):

    name = models.CharField('To Do List name', max_length=200)

    def __str__(self):
        return self.name

class Item2(models.Model):

    text = models.CharField(max_length=300)
    todolist2 = models.ForeignKey(ToDoList2, related_name='item', blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.text
