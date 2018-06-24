from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views.generic import View, ListView, DetailView
from django.shortcuts import render
import json
from constructor.models import Constructed, Part, PartsInPlace
from draw import draw


class IndexView(View):
    template_name = 'constructor/index.html'

    # display blank form
    def get(self, request):
        return render(request, self.template_name, None)

    # process from data
    #def post(self, request):

class Constructor(View):
    template_name = 'constructor/Syndicate.html'
    def get(self, request):
        return render(request, self.template_name, None)

    #def post(self,request):
        #somedata = request.POST['sometext']
        #return render_to_response


class Builder(View):
    template_name = 'constructor/Syndicate.html'
    def get(self, request):
        return render(request, self.template_name, None)


    def post(self,request):
        c = {}
        #c.update(csrf(request))
        print("Сюда все таки обратилось")
        #data = serializers.serialize('json',)
        #print(json.loads(request.body.decode('utf-8')))
        data_unicode = request.body.decode('utf-8')
        #print(data_unicode)
        data = json.loads(request.body)
        #print(data)

        chest = data['chest']
        height = data['height']
        neck = data['neck']
        sleeve = data['sleeve']
        shoulder= data['shoulder']

        print(chest, height, neck, sleeve, shoulder)
        product = Constructed()
        product.user = request.user
        product.chest = chest
        product.height = height
        product.neck = neck
        product.sleeves = sleeve
        product.shoulder = shoulder



        blueprint = draw(int(chest),int(height),int(neck),int(sleeve),int(shoulder))

        product.save()

        image_field = product.blueprint
        img_name = 'my_image.png'
        image_field.save(img_name, InMemoryUploadedFile(blueprint,None,img_name,'image/png', blueprint.tell,None))

        for d in data['details']:
            naming = d['name']
            if(naming!='Main' and naming!='Plane'):
                detail = PartsInPlace()
                detail.part = Part.objects.get(name = naming)
                detail.constructed = product
                tsr = json.loads(d['tsr'])
                #print(tsr['0'])
                detail.x = tsr['0']
                detail.y = tsr['1']
                detail.z = tsr['2']
                detail.s = tsr['3']
                detail.qx = tsr['4']
                detail.qy = tsr['5']
                detail.qz = tsr['6']
                detail.qw = tsr['7']
                detail.save()
                print(detail.part, detail.constructed)
        return render(request, self.template_name, c)




class Report(ListView):
    template_name = "constructor/report.html"
    context_object_name = 'cons'



    def get_queryset(self):
        return Constructed.objects.all().order_by("-created_date")


class Generator(DetailView):
    model = Constructed
    template_name = "constructor/generator.html"



