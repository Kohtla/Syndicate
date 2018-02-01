from django.views import generic
from .models import Theme, Message
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
class IndexView(generic.ListView):
    template_name = 'forum/index.html'
    context_object_name = 'themes'

    def get_queryset(self):
        return Theme.objects.all()


class DetailView(generic.DetailView):
    model = Theme
    template_name = 'forum/theme_detail.html'

class ThemeCreate(CreateView):
    model = Theme
    fields =['creator', 'theme_title', 'theme_image']

class UserFormView(View):
    form_class = UserForm
    template_name = 'forum/registration_form.html'

    #display blank form
    def get(self, request):
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
