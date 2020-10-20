import requests
import os
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        self.file_path = file_path

        response = requests.get(\
        "https://cloud-api.yandex.net/v1/disk/resources/upload", \
        params={"path": file_path},\
        headers= {"Authorization": f"OAuth {self.token}"})

        link = response.json()["href"]

        response = requests.put(link, \
        files={"file": open(file_path, "rb")},\
        headers={"Authorization": f"OAuth {self.token}"})

        return f' Ваш {file_path} , был успешно загружен'

if __name__ == '__main__':
    uploader = YaUploader('ThisisTOKEN)
    result = uploader.upload('test.txt')
    print(result)