#author_by zhuxiaoliang
#2018-11-11 下午3:49

from django.urls import path,re_path
from .views import class_list,class_add,class_delete,class_delete_confirm,class_edit,class_edit_confirm

from .views import student_list,student_add,student_edit,student_delete

from .views import teacher_list,teacher_add

from .views import user_add


app_name = 'student'
urlpatterns=[

    path('class_list/',class_list,name='class_list'),
    path('class_add/',class_add,name='class_add'),
    re_path('class_delete/(\d+)/',class_delete,name='class_detele'),
    path('class_delete_confirm/',class_delete_confirm,name='class_delete_confirm'),
    re_path('class_edit/(\d+)/',class_edit,name='class_edit'),
    path('class_edit_confirm/',class_edit_confirm,name='class_edit_confirm'),
    path('student_list/',student_list,name='student_list'),
    path('student_add/',student_add,name='student_add'),
    re_path('student_edit/(\d+)/',student_edit,name='student_edit'),
    re_path('studnent_delete/(.+)/',student_delete,name='student_delete'),
    path('teacher_list',teacher_list,name='teacher_list'),
    path('teacher_add/',teacher_add,name='teacher_add'),
    path('user_add/',user_add,name='user_add'),
]