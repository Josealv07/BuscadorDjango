import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    #request -> HttpRequest -> django
    #request.body
    body = request.body #byte string of JSON data
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    data['params'] = dict(request.GET)
    data['content_type'] = request.content_type
    data['Message'] = "Esta es tu data"
    return JsonResponse(data)
