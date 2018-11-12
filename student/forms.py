#author_by zhuxiaoliang
#2018-11-11 下午2:46

from django.forms import fields,widgets,Form
from .models import Students,Classes,Teachers

class Classes_Form(Form):
    id = fields.IntegerField(error_messages={'required':'ID不能修改'})
    title = fields.CharField(
                              min_length=2,
                              required=True,
                              error_messages={
                                  'min_length':'长度大于2',
                                  'required':'不能为空',
                              }
                              )

class Students_Form(Form):
    sname = fields.CharField(required=True,
                            widget=widgets.TextInput(attrs={'class':'form-control'}),
                            error_messages={
                                'required':'姓名不能为空',
                            }

                            )
    sex = fields.CharField(required=True,error_messages={'required':'性别不能为空'},
                            widget = widgets.TextInput(attrs={'class':'form-control'}))

    class_id = fields.IntegerField(widget=widgets.Select(choices=Classes.objects.values_list('id','title'),attrs={'class':'form-control'}))


class Teachers_Form(Form):
    tname = fields.CharField(required=True,error_messages={'required':'姓名不能为空'})

    class_id = fields.MultipleChoiceField(choices=Classes.objects.values_list('id','title'),widget=widgets.SelectMultiple,error_messages={'required':'不能为空'})

    def __init__(self,*args,**kwargs):
        super(Teachers_Form,self).__init__(*args,**kwargs)
        self.fields['class_id'].choices=Classes.objects.values_list('id','title')


class Test_Form(Form):
    name = fields.CharField()
    text = fields.CharField(widget=widgets.Textarea,)
    age = fields.CharField(widget=widgets.CheckboxInput)
    hobly = fields.MultipleChoiceField(
        choices=[(1,'篮球'),(2,"足球"),(3,"高俅")],
        widget=widgets.CheckboxSelectMultiple
    )
    sex = fields.MultipleChoiceField(
        choices=[(1,'男'),(2,'女')],
        widget=widgets.RadioSelect
    )
