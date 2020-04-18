from django import forms
from .models import User_Profile

class Profile_Form(forms.ModelForm):
	class Meta:
		model = User_Profile
		fields = [
		'Name',
		'RollNo',
		'Email',
		'Subject',
		'Assignment'
		]