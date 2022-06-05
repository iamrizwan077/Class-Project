from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "required": "",
            "name": "username",
            "id": "username",
            "type": "text",
            "class": "form-input",
            "placeholder": "Username",
            "maxlength": "64",
            "minlength": "6"
        })
        self.fields["email"].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'placeholder':'JohnDoe@mail.com',
        })
        self.fields["password1"].widget.attrs.update({
            "required": "",
            "name": "password1",
            "id": "password1",
            "type": "password",
            "class": "form-input",
            "placeholder": "Password",
            "maxlength": "22",
            "minlength": "8"
        })
        self.fields["password2"].widget.attrs.update({
            "required": "",
            "name": "username",
            "id": "password",
            "type": "password",
            "class": "form-input",
            "placeholder": "Password",
            "maxlength": "22",
            "minlength": "8"
        })

    class Meta:
        model = User
        fields = ('username','email','password1','password2',)












































































































      

"""
class RegisterForm(forms.Form):
      username= forms.CharField(widget= forms.TextInput(attrs={ 
          'class': 'form-input', 
          'required':'', 
          'name':'username', 
          'id':'username', 
          'type':'text', 
          'placeholder':'John Doe', 
          'maxlength': '24', 
          'minlength': '6', 
			}  
    ))
      email= forms.EmailField(widget= forms.EmailInput(attrs={ 
          'class': 'form-input', 
          'required':'', 
          'name':'email', 
          'id':'email', 
          'type':'email', 
          'placeholder':'example@gmail.com'
			}  
    ))
      password1= forms.PasswordInput(attrs={ 
          'class': 'form-input', 
          'required':'', 
          'name':'password1', 
          'id':'password1', 
          'type':'password', 
          'placeholder':'Password', 
          'maxlength': '24', 
          'minlength': '6', 
			}  
    )
username= forms.CharField(widget= forms.TextInput(attrs={ 
          'class': 'form-input', 
          'required':'', 
          'name':'username', 
          'id':'username', 
          'type':'text', 
          'placeholder':'John Doe', 
          'maxlength': '24', 
          'minlength': '6', 
			}  
    ))
"""