import os
import requests
import zipfile

def download_movielens():
    dataset_url = "http://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
    dataset_zip = "ml-latest-small.zip"
    dataset_folder = "ml-latest-small"

    if not os.path.exists(dataset_folder):
        print("Descargando dataset MovieLens...")
        r = requests.get(dataset_url)
        with open(dataset_zip, 'wb') as f:
            f.write(r.content)

        print("Descomprimiendo dataset...")
        with zipfile.ZipFile(dataset_zip, 'r') as zip_ref:
            zip_ref.extractall(".")
        print("Dataset descargado y listo en la carpeta 'ml-latest-small'")
    else:
        print("El dataset ya existe en la carpeta local.")

if __name__ == "__main__":
    download_movielens()
