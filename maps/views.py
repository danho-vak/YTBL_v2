import json

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render

from maps.models import Coordinates


def showMap(request):
    temp_object_list = None
    type_code = request.GET.get('type_code', None)
    if type_code == '1':
        temp_object_list = Coordinates.objects.filter(type_code=1)
    elif type_code == '2':
        temp_object_list = Coordinates.objects.filter(type_code=2, is_next_to=True)
    else:
        temp_object_list = Coordinates.objects.all()

    cords_json = json.dumps(list(temp_object_list.values()), ensure_ascii=False, cls=DjangoJSONEncoder)

    return render(request, 'maps/map.html', {'data': cords_json})