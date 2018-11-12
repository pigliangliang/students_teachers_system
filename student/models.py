from django.db import models

# Create your models here.

class Classes(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class Students(models.Model):
    sname = models.CharField(max_length=64)
    sex = models.CharField(max_length=32)
    class_id = models.ForeignKey(Classes,on_delete=True)

class Teachers(models.Model):
    tname = models.CharField(max_length=64)
    class_id = models.ManyToManyField(Classes)

######
class Department(models.Model):
    title = models.CharField(max_length=128,verbose_name='部门名称')

    def __str__(self):
        return self.title

class UserInfor(models.Model):
    name = models.CharField(max_length=64,verbose_name='姓名')
    email = models.EmailField(max_length=32,verbose_name='邮箱')
    department = models.ForeignKey(Department,verbose_name='部门名称',on_delete=True)

    def __str__(self):
        return self.name

