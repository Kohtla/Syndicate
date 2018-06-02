from django.http import HttpResponseRedirect
from django.views import generic
from .models import Theme, Message
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm, LoginUserForm, SendMessageForm
from django.contrib.auth import logout
from django.contrib import messages


class IndexView(generic.ListView):
    template_name = 'forum/index.html'
    context_object_name = 'themes'

    def get_queryset(self):
        return Theme.objects.all()


class DetailView(generic.DetailView):
    model = Theme
    template_name = 'forum/theme_detail.html'
    form_class = SendMessageForm



    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        form = self.form_class(None)
        context['form'] = form
        return context

    #def get(self, request):

       # return render(request, self.template_name, {'form':form})

    def post(self,request,pk):
        form = self.form_class(request.POST)
        message = Message()
        theme = Theme()
        if form.is_valid():

            message.theme = Theme.objects.get(pk = pk)
            message.author = request.user
            message.message_text = form.cleaned_data['message_text']
            message.save()
            return render(request, self.template_name, {'form': form})

class ThemeCreate(CreateView):
    model = Theme
    fields =['creator', 'theme_title', 'theme_image']

class UserFormView(View):
    form_class = UserForm
    template_name = 'forum/registration_form.html'

    #display blank form
    def get(self, request: object) -> object:
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    #process from data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return User objects if credentials(полномочия) are correct
            user = authenticate(username = username, password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('forum:index')

        return render(request, self.template_name, {'form': form})

class Log_out(View):
    def get(self, request: object) -> object:
        logout(request)
        return redirect('main:index')

class Log_in(View):
    form_class = LoginUserForm
    template_name = 'forum/login_form.html'
    def get(self, request: object) -> object:
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
            # normalized data
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']


            #return User objects if credentials(полномочия) are correct
            user = authenticate(username = username, password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('main:index')
        messages.error(request,'The password is wrong or this user does not exist...')
        return render(request, self.template_name, {'form': form})


