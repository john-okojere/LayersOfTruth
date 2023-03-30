from django import forms
from .models import Academics


class AcademicForm(forms.ModelForm):
    class Meta:
        model = Academics
        fields = ('School','matric_number','faculty','department','program','time_table','lvl1_cgpa','lvl2_cgpa','lvl3_cgpa','lvl4_cgpa','lvl5_cgpa')
    