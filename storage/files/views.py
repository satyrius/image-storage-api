from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import UploadFileForm


@require_POST
@csrf_exempt
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.files['file']
            return JsonResponse({
                'name': file.name,
                'size': file.size,
            })
        else:
            return JsonResponse({'errors': form.errors}, status=400)
