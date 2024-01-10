import requests
import zipfile
import io
import os
from .utils import paths
from dotenv import load_dotenv

load_dotenv()

SERVER_URL = os.getenv("PRIVATE_SERVER_URL")


def test():
    url = f"http://37.27.7.58:5000/download_zip/qXl7C1nV"
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_ref:
        zip_ref.extractall(paths.inputs_folder)


def download_zip(session_id):
    url = f"{SERVER_URL}/download_zip/{session_id}"
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_ref:
        zip_ref.extractall(paths.inputs_folder)

    response = requests.delete(
        f"{SERVER_URL}/delete_files/{session_id}")
    print(response.json())
