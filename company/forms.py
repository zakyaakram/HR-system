from django import forms
from .models import departments 
from .models import branches


class newDepartmentToBrancheForm(forms.ModelForm):
    
    class Meta:
        model = departments
        fields = ['name','description']


class editDepartmentToBrancheForm(forms.ModelForm):
    
    class Meta:
        model = departments
        fields = ['name','description']

#class EditBranchForm(forms.ModelForm):
    #class Meta:
      #  model = branches
      #  fields = ['name', 'address', 'phone', 'email']        

class EditBranchForm(forms.ModelForm):
    class Meta:
        model = branches
        fields = ['name', 'address', 'phone', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }