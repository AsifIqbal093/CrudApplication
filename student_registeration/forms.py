from django import forms
from .models import StudentInfo

class StudentForm(forms.ModelForm):

    class Meta:
        model = StudentInfo
        fields= ('std_name','std_fname','std_phone', 'std_program')
        labels = {
            'std_name':'Student Name',
            'std_fname':'Father Name',
            'std_phone':'Phone',
            'std_program':'Program'
        }

    def __init__(self, *args, **kargs):
        super(StudentForm,self).__init__(*args, **kargs)
        self.fields['std_program'].empty_label = 'Select'
        self.fields['std_phone'].required = False

