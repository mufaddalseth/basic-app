from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home', views.home , name = "home"),
    path('', views.history , name = "history"),
    path('list', views.course_list , name = "list"),
    path('delete/<int:id>', views.delete_course , name = "delete"),
    path('course-create', views.courses , name = "courses"),
    path('edit/<int:id>', views.edit_course , name = "editit"),
    path('edit/<int:id>', views.edit_it , name = "edit"),


    ]


