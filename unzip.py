import zipfile
with zipfile.ZipFile("foyezrabbi.zip","r") as zip_ref:
    zip_ref.extractall("foyezrabbi")