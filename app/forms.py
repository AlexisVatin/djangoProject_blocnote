from django import forms
from app.models import Post, Person


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'message')


class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))

    class Meta:
        model = Person
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur'}))
    mail = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'mail@mail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmer mot de passe'}))

    class Meta:
        model = Person
        fields = ('username', 'mail', 'password', 'password_confirm')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.isalnum():
            self.add_error('username', 'Invalid characters')
            return None
        return username

    def clean(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password != password_confirm:
            self.add_error('password', 'passwords do not match')
            return None
        return super().clean()
