import json

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render

from maps.models import Coordinates

'''
    function :
        showMap : DB에서 좌표 데이터를 가져와 templates/maps/map.html로 값을 넘겨주는 function
    
    args :
        temp_object_list : QuerySet을 받을 변수
        type_code : get방식으로 url 파라미터를 받을 변수
        cords_json : QuerySet을 list로 캐스팅 후 json으로 변환한 데이터를 가질 변수
'''

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