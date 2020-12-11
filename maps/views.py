import json

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render

from maps.models import Coordinates

def showMap(request):
    temp_object_list = None
    type_code = request.GET.get('type_code', None)
    if type_code == '1':
        temp_object_list = Coordinates.objects.filter(type_code=1) | Coordinates.objects.filter(is_next_to=True)
    elif type_code == '2':
        temp_object_list = Coordinates.objects.filter(type_code=2) | Coordinates.objects.filter(is_next_to=True)
        print(temp_object_list)
    else:
        temp_object_list = Coordinates.objects.all()

    cords_json = json.dumps(list(temp_object_list.values()), ensure_ascii=False, cls=DjangoJSONEncoder)

    return render(request, 'maps/map.html', {'data': cords_json})