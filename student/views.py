from django.shortcuts import render
from django.shortcuts import render_to_response,HttpResponse,reverse
# Create your views here.
from .models import Classes,Teachers,Students
from .forms import Classes_Form,Students_Form,Teachers_Form,Test_Form
from django.http import HttpResponseRedirect



def class_list(request):
    if request.method=="GET":
        c_list  =Classes.objects.all()
        return render_to_response('class_list.html',{'clist':c_list})

def class_add(request):
    if request.method=="POST":
        class_form = Classes_Form(request.POST)
        #print(class_form)
        if class_form.is_valid():
            print(class_form.cleaned_data)
            try:
                  Classes.objects.create(**class_form.cleaned_data)
                  return HttpResponse(1)
                  #return HttpResponse('{"status":"success"}')
                  #return HttpResponseRedirect(reverse('student:class_list'))
            except Exception as e:
                # import json
                # ret = {
                #     'status':'failed',
                #     'msg':e
                # }
                # return HttpResponse(json.dumps(e),content_type='application/json')
                return HttpResponse('提示：添加失败，班级号重复')
        else:


            return HttpResponse('提示：添加失败，班级ID必填且整数，班级名称必填且为中文')

    else:
        class_form = Classes_Form()
        return render_to_response('class_add.html',{'class_form':class_form})


def class_delete(request,id):
    item = Classes.objects.get(id__exact=id)
    item.delete()
    return HttpResponseRedirect(reverse('student:class_list'))
def class_delete_confirm(request):#use ajax
    id = request.POST.get('id')
    try:
        Classes.objects.get(id__exact=id).delete()
        return HttpResponse(1)
    except Exception as e:
        return HttpResponse(e)
def class_edit(request,id):
    if request.method=="GET":
        class_item = Classes.objects.get(id__exact=id)
        class_form = Classes_Form(initial={'id':id,'title':class_item.title})
        return  render_to_response('class_edit.html',{'class_form':class_form,'id':id})
    else:
        class_form = Classes_Form(request.POST)
        print(class_form)
        if class_form.is_valid():
            Classes.objects.filter(id__exact=id).update(**class_form.cleaned_data)
            return HttpResponseRedirect(reverse('student:class_list'))
        else:
            print('error')
            return render_to_response('class_edit.html',{'class_form':class_form,'id':id})

def class_edit_confirm(request):#use ajax
    id =request.POST.get('id')
    title = request.POST.get('title')
    print(id,title)
    Classes.objects.filter(id__exact=id).update(id=id,title=title)
    return HttpResponse(1)

def student_list(requst):
    if requst.method=="GET":
        students = Students.objects.all()
        return render_to_response('student_list.html', {'students':students})

def student_add(request):
    if request.method=='POST':
        student_form = Students_Form(request.POST)
        if student_form.is_valid():
            print(student_form.cleaned_data)
            class_id = student_form.cleaned_data.get('class_id')
            student_class = Classes.objects.get(id__exact=class_id)
            #向一对多表中查数据
            s = Students(sname=student_form.cleaned_data.get('sname'),sex=student_form.cleaned_data.get('sex'),class_id=student_class)
            s.save()
            return HttpResponseRedirect(reverse('student:student_list'))
        else:
            student_form = Students_Form()
            return render_to_response('student_add.html', {'student_add': student_form})
    else:
        student_form = Students_Form()
        return render_to_response('student_add.html',{'student_add':student_form})

def student_edit(request,id):
    if request.method=="POST":
        sname = request.POST.get('sname')
        s = Students.objects.filter(sname=sname)

        student_form = Students_Form(request.POST)
        if student_form.is_valid():
            s.update(**student_form.cleaned_data)
        return HttpResponseRedirect(reverse('student:student_list'))
    else:
        student = Students.objects.filter(class_id=id).first()
        class_id = Classes.objects.get(id__exact=id)
        student_form = Students_Form(initial={'sex':student.sex,'sname':student.sname,'class_id':class_id,'id':id})
        return render_to_response('student_edit.html',{'student_form':student_form})

def student_delete(request,name=None):
    """
    model 中设计student表时存在缺陷，没有唯一主键
    这里假定名字可以唯一确认一名学生
    :param request:
    :param name:
    :return:
    """
    print(name)
    s = Students.objects.filter(sname=name)
    s.delete()
    return HttpResponseRedirect(reverse('student:student_list'))


def teacher_list(request):
    if request.method=="GET":
        teacher = Teachers.objects.all()
        d = {}
        for teach in teacher:
            print(teach.id,teach.tname)
            t = Teachers.objects.get(id=teach.id)
            print(t.class_id.all().values_list())
            c = t.class_id.all().values_list().filter()
            for i in c:
                print('iii',i)
                if teach.id not in d.keys():
                    d[teach.id]=[i]
                else:
                    d[teach.id].append(i)

        print(d)
        return render_to_response('teacher_list.html',{'teacher':teacher,'d':d})

def teacher_add(request):
    if request.method=="POST":
        teacher_form = Teachers_Form(request.POST)
        if teacher_form.is_valid():
            tname = teacher_form.cleaned_data.get('tname')
            class_id  = teacher_form.cleaned_data.get('class_id')
            print(tname,class_id)
            #
            teacher = Teachers(tname=tname)
            teacher.save()
            for id in class_id:
                class_teacher = Classes.objects.get(id__exact=id)
                teacher.class_id.add(class_teacher)
            teacher.save()

            return HttpResponseRedirect(reverse('student:teacher_list'))
        else:
            teacher_form = Teachers_Form()
            return render_to_response('teacher_add.html', {'teacher_form': teacher_form})
    else:
        teacher_form = Teachers_Form()
        return  render_to_response('teacher_add.html',{'teacher_form':teacher_form})


#########

from .models import Department,UserInfor
from django.forms import ModelForm

class UserModelForm(ModelForm):
    class Meta:
        model = UserInfor

        fields= '__all__'
def user_add(request):
    if request.method=="POST":
        uf = UserModelForm(request.POST)
        if uf.is_valid():

            dp =Department.objects.get(title=uf.cleaned_data.get('department'))
            s = UserInfor.objects.create(name=uf.cleaned_data.get('name'),email=uf.cleaned_data.get('email'),department=dp)
            s.save()
            return HttpResponse('ok')
    else:
        uf = UserModelForm()
        return render_to_response('user_add.html',{'uf':uf})



