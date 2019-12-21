from django.conf.urls import url
from django.contrib import admin
from main import views
from django.urls import path

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  url(r'^add_todo/', views.add_todo),
  path('todo_delete/<int:todo_id>', views.todo_delete),
]
