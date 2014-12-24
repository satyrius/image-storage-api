from django.http import JsonResponse
from .forms import UploadFileForm


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
