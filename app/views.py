from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from app.forms import PostForm, LoginForm, RegisterForm
from django.views.generic import TemplateView, DetailView, ListView, FormView
from django.urls import reverse
from app.models import Post, Person

# Create your views here.
from django.views.generic import TemplateView


class FirstView(TemplateView):
    template_name = 'first.html'


class LogView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        return render(self.request, self.template_name)


class RegisterView(FormView):
    pass


class BoardView(ListView):
    pass


class PostDetailView(DetailView):
    model = Post
    template_name = 'viewpost.html'


def postcreate(request):
    pass


def postedit(request, pk, template_name='edit.html'):
    pass


def postdelete(request, pk, template_name='delete.html'):
    pass
