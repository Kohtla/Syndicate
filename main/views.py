from django.views.generic import View
from django.shortcuts import render

# Create your views here.
class IndexView(View):
    template_name = 'main/index.html'

    # display blank form
    def get(self, request: object) -> object:
        return render(request, self.template_name, None)