# list down 2 standard library modules for zipping and unzipping files.
# zipfile is best one by one for writing single file.

import zipfile

with zipfile.ZipFile('files.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write('README.md')
    my_zip.write('speedtest-demo.py')

with zipfile.ZipFile('files.zip', 'r') as my_zip:
    my_zip.extractall('files')

# shutil is best for writing files in one directory.
#import shutil
# shutil.make_archive('another','zip','files')
# shutil.unpack_archive('another.zip','another')
