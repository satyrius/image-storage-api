from django.http import JsonResponse


def upload(request):
    return JsonResponse({
        'foo': 'bar'
    })
