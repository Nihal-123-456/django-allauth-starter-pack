import requests
from pathlib import Path

def download_flowbite_files(url:str, download_path:Path, parent_mkdir:bool=True):
    if parent_mkdir:
        # if the download folder is not already created then this will create it in the designated location
        download_path.parent.mkdir(parents=True, exist_ok=True) 
    try:
        response = requests.get(url)
        response.raise_for_status()
        # the files are being written to the download_path
        download_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f'failed to download {url}:{e}')
        return False

