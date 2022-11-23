from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "type":"text",
            "class":"form-control",
            "id":"inputUsername",
            "aria-label":"Username",
            "aria-describedby":"usernameHelp",
            "placeholder":"닉네임을 입력하세요",
            "maxlength":"8",
        })
        self.fields["email"].widget.attrs.update({
            "type":"email",
            "required":"",
            "class":"form-control",
            "id":"inputEmail",
            "aria-describedby":"emailHelp",
            "placeholder":"Choice@movie.com",
            "maxlength":"30",
        })
        self.fields["password1"].widget.attrs.update({
            "type":"password", 
            "required":"",
            "id":"inputPassword1", 
            "class":"form-control",
            "aria-describedby":"passwordHelpInline1",
            "for":"InputPassword1",
            "maxlength":"22",
            "minlength":"8",

        })
        self.fields["password2"].widget.attrs.update({
            "type":"password", 
            "required":"",
            "id":"inputPassword2", 
            "class":"form-control",
            "aria-describedby":"passwordHelpInline2",
            "for":"InputPassword2",
            "maxlength":"22",
            "minlength":"8",
        })

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "type":"text",
            "class":"form-control",
            "id":"inputUsername",
            "aria-label":"Username",
            "aria-describedby":"usernameHelp",
            "placeholder":"닉네임을 입력하세요",
        })
        self.fields["password"].widget.attrs.update({
            "type":"password", 
            "required":"",
            "id":"inputPassword", 
            "class":"form-control",
            "aria-describedby":"passwordHelpInline1",
            "for":"InputPassword",
            "maxlength":"22",
            "minlength":"8",
        })