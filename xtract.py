from sys import argv
from shutil import copyfile
import os
import zipfile



Script, file_name = argv

def x_unzip(file_name):
    file_rename = file_name + '.zip'
    copyfile(file_name, file_rename)
    zip = zipfile.ZipFile(file_rename, 'r')   
    path = os.getcwd() + os.sep + '\\XTRACT_%s\\' % file_name + os.sep
    zip.extractall(path)
    zip.close()
    
def main():
    x_unzip(file_name)
           
if __name__ == "__main__":
        main()