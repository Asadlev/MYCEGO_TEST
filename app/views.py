from django.shortcuts import render, HttpResponse
from .yandex_disk_api import YandexDiskAPI
from django.views.decorators.cache import cache_page


@cache_page(60*15)
def file_list(request):
    public_key = request.GET.get('public_key')
    files = []
    if public_key:
        api = YandexDiskAPI(public_key)
        files = api.get_files()
    return render(request, 'app/file_list.html', {'files': files, 'public_key': public_key})

def download_file(request, path):
    public_key = request.GET.get('public_key')
    api = YandexDiskAPI(public_key)
    file_content = api.download_file(path)
    response = HttpResponse(file_content, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{path.split("/")[-1]}"'
    return response
