import os
from math import ceil

'''
This was just a quick script that I wrote to split a list of endpoints into multiple sub-lists of endpoints
that could be passed to Burp Scanner.
The script could be improved by:
1. Removing the hardcoded paths and automatically creating the required directories.
2. Allowing the required data to automatically be read from Burp project files.
'''

if len(os.sys.argv) < 2:
    exit(-1)

vulntype = os.sys.argv[1]
username = os.getlogin()

with open(r'C:\\Users\\'+username+'\\Desktop\\scan-endpoints\\'+vulntype+'\\'+vulntype+'-endpoints.txt') as f:
    contents = f.readlines()
    CHUNK_SIZE = 20
    chunk_index = ceil(len(contents)/CHUNK_SIZE)
    IPS = ["192.168.2."+str(i) for i in range(100,100+CHUNK_SIZE)]
    scan_index = 1
    while len(contents) > 0:
        chunk = contents[:chunk_index]
        with open(r'C:\\Users\\'+username+'\\Desktop\\scan-endpoints\\'+vulntype+'\\'+vulntype+'-scan'+str(scan_index)+'.txt','w') as g:
            host = 'https://' + IPS[scan_index-1] + ':8443'
            chunks = []
            for line in chunk:
              to_write = host + line
              if not to_write in chunks:
                  g.write(to_write)
                  chunks.append(to_write)
        contents = contents[chunk_index:]
        scan_index += 1
