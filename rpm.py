#!/usr/bin/python
# Acts like rpm -qa and lists the names of all the installed packages.
# Usage:
# python rpmqa.py

# import rpm
# import os
#
# def makedir (dir_path: str) -> str:
#         if not os.path.exists('dir_path'):
#                 os.makedirs('dir_path')
#         print(dir_path)
#
# dir_for_download='~/build/rpm'
# dir_store_rebuild='~/build/packages'
#
# makedir(dir_for_download)
# makedir(dir_store_rebuild)

#url= ftp://centos.colocall.net/centos/7/os/x86_64/Packages/
# os.system ('wget -r -np -nd -A rpm %s')

import os


folder_download= "/home/dasha/build/rpm"
folder_saverpm= "/home/dasha/build/packages"

def make_folders(folders):
    try:
        os.makedirs(os.path.expanduser(folders))
    except OSError:
        print("Creation of the directory %s failed" % folders)
    else:
        print("Successfully created the directory %s " % folders)

make_folders (folder_download)
make_folders (folder_saverpm)

current_path = os.getcwd()
print ("The current working directory is %s" % current_path)


print ("Directory changed %s" % os.chdir(folder_download))
current_path = os.getcwd()
print ("The current working directory is %s" % current_path)

#url = "ftp://centos.colocall.net/centos/7/os/x86_64/Packages/"
#os.system('wget -r -np -nd -l1 --no-parent -A rpm %s'%url)