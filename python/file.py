import zipfile
def compressZip(zipname, filename) :

    with zipfile.ZipFile(zipname, 'w') as ziph :
     ziph.extractall()

filename = input("파일이름을 입력하시오: ")
zipname = filename + '.zip'
compressZip(zipname, filename)