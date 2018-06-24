from django.views.generic import View
from django.shortcuts import render
import json
from constructor.models import Constructed, Part, PartsInPlace


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
        product.chest = chest
        product.height = height
        product.neck = neck
        product.sleeves = sleeve
        product.shoulder = shoulder
        product.save()


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

