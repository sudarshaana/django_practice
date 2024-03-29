from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    #print(request.POST)
    all_todo = Todo.objects.all().order_by("-added_date")
    content = {"all_todo": all_todo}
    return render(request, 'main/index.html', content)

# @csrf_exempt
def add_todo(request):
  #print(request.POST)
  added_date = timezone.now()
  content = request.POST["text"]

  Todo.objects.create(added_date = added_date, text = content)
  return HttpResponseRedirect("/")

def todo_delete(request, todo_id):
  Todo.objects.get(id=todo_id).delete()
  return HttpResponseRedirect("/")

def todo_edit(request, todo_id):
  obj = Todo.objects.get(id=todo_id)

  if request.method == "POST":
    content = request.POST["text"]
    obj.text = content
    obj.save()
    return HttpResponseRedirect("/")

  text = obj.text
  content = {"text": text}
  print(obj)
  print(content)
  return render(request, 'main/edit.html', content)
