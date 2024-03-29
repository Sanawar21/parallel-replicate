import requests
import zipfile
import io
import os
import subprocess
from .utils import paths
from dotenv import load_dotenv

load_dotenv()

SERVER_URL = os.getenv("PRIVATE_SERVER_URL")


def test():
    url = "https://drive.google.com/uc?export=download&id=1f_Mw-xp_xCdyKxgROPqTX5C2SK5XyEKs"
    wget_command = f"wget -O - {url}"
    wget_process = subprocess.Popen(
        wget_command, shell=True, stdout=subprocess.PIPE)

    with zipfile.ZipFile(io.BytesIO(wget_process.communicate()[0]), 'r') as zip_ref:
        zip_ref.extractall(paths.inputs_folder)


def download_zip(session_id):
    url = f"{SERVER_URL}/download_zip/{session_id}"
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_ref:
        zip_ref.extractall(paths.inputs_folder)

    response = requests.delete(
        f"{SERVER_URL}/delete_files/{session_id}")
    print(response.json())
