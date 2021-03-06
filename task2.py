import requests
import os
from pprint import pprint
import yadisk

class YaUploader:
    def __init__(self, token: str , folder: str, file: str):
        self.token = token
        self.folder = folder
        self.file = file

    def upload(self):
        """Метод загруджает файл file_path на яндекс диск"""

        y = yadisk.YaDisk(token=self.token)

        # Проверяет, валиден ли токен
        print(y.check_token(self.token))
        try:
            y.mkdir(self.folder)
            y.upload(self.file, f"{self.folder}/{self.file}")
        except:
            y.upload(self.file, f"{self.folder}/{self.file}")

        return f'Ваш файл {self.file}, успешно загружен в папку {self.folder}'

if __name__ == '__main__':
    file = open(rb"\Users\User\Desktop\4.txt", "rb")
    # Передаем токен, директорию, название файла
    uploader = YaUploader('ThisisTOKEN',  "/hw_api" , file)
    # Вызываем метод upload
    print(uploader.upload())