"""
Lab09 - polecenia systemowe
"""

import os

print(os.listdir("/Users/polya.bragina/Desktop"))

path = os.path.join(os.path.expanduser("~"), "Test")
print(path)

#os.mkdir(path, 0o777)
print(os.listdir(os.path.expanduser("~")))

path2 = os.path.join(os.path.expanduser("~"), "test_")
os.rename(path, path2)
print(os.listdir(os.path.expanduser("~")))

(katalog,plik) = os.path.split("/Users/polya.bragina/Desktop/..")
print(katalog)
print(plik)

(katalog,roz)=os.path.splitext(plik)
print(katalog)
print(roz)

os.mkdir(path2)
print(os.listdir(os.path.expanduser("~")))