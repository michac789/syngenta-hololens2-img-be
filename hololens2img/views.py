from django.http import JsonResponse
from django.views import View
from hololens2img.models import MS1, MS2, MS3, MS4, MS5, MS6, WH


class CustomImageView(View):
    def get(self, _):
        instances = self.model.objects.all().order_by('order')
        return JsonResponse({
            "count": instances.count(),
            "data": [instance.serialize() for instance in instances]
        })

class MS1View(CustomImageView):
    model = MS1

class MS2View(CustomImageView):
    model = MS2

class MS3View(CustomImageView):
    model = MS3

class MS4View(CustomImageView):
    model = MS4

class MS5View(CustomImageView):
    model = MS5

class MS6View(CustomImageView):
    model = MS6
    
class WHView(CustomImageView):
    model = WH
