import requests
from typing import List, Dict

class YandexDiskAPI:
    BASE_URL = "https://cloud-api.yandex.net/v1/disk/public/resources"

    def __init__(self, public_key: str):
        self.public_key = public_key

    def get_files(self):
        """Получает список файлов и папок по публичной ссылке."""
        params = {'public_key': self.public_key}
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json().get('_embedded', {}).get('items', [])
    
    def download_file(self, path: str) -> bytes:
        """Скачивает файл с Яндекс.Диска."""
        params = {'public_key': self.public_key, 'path': path}
        response = requests.get(f"{self.BASE_URL}/download", params=params)
        response.raise_for_status()
        download_url = response.json().get('href')
        file_response = requests.get(download_url)
        file_response.raise_for_status()
        return file_response.content
