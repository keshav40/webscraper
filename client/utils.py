import requests
import os

def download_image(url, filename=None):
    os.makedirs("images", exist_ok=True)

    response = requests.get(url, stream=True)
    with open(filename, "wb+") as file:
        for chunk in response.iter_content(1024):
            file.write(chunk)

    return filename
