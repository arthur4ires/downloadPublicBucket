from os import chdir, write
import requests
from threading import Thread
from xml.etree import ElementTree

urlBucket = 'xD'

def writeFile(urlDownload):
    global urlBucket

    urlFile = '{}/{}'.format(urlBucket, urlDownload)
    
    print(urlFile)
    
    downloadFile = requests.get(urlFile, verify = False)

    writeFile = open('bucket_amazon/{}'.format(urlDownload.replace('/','_')), 'w')
    writeFile.write(downloadFile.text)

def main():
    for child in ElementTree.fromstring(requests.get(urlBucket, verify = False).content):
        for key, newChild in enumerate(child):
            if key == 0:
                
                Thread(target=writeFile, args=(newChild.text,)).start()

                continue

if __name__ == "__main__":
    main()
