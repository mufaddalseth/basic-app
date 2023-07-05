from django import forms
from courses_section.models import Courses

class Courses_Form(forms.ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'
        # fields = ['name']
        
        