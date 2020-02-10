#!/usr/bin/env python
"""nebula.py: your packets are not what they seem..."""
__credits__ = ["Slack Engineering"]
__license__ = "Internal"
__version__ = "0.0.5"
__email__ = "josh@joshhighet.com"
__status__ = "Pilot"
__nebula_credits__ = "https://github.com/slackhq/nebula"
__nebula_whitepaper__ = "https://medium.com/p/884110a5579"
###########
# modules #
###########
import os
import glob
import tarfile
import platform
import subprocess
import urllib.request
###########
#base vars#
###########
caname = "joshhighet"
nebversion="1.0.0"
repo = "https://github.com/slackhq/nebula/releases/download/v"
amd64 = "nebula-linux-amd64.tar.gz"
arm64 = "nebula-linux-arm64.tar.gz"
arm6 = "nebula-linux-arm6.tar.gz"
arm = "nebula-linux-arm.tar.gz"
darwin = "nebula-darwin-amd64.tar.gz"
windows = "nebula-windows-amd64.tar.gz"
filename= "nebula-joshhighet.tar.gz"
#set handler for when an interaction shows the prior presence of nebula utilities
def previousinstall():
    print("The installer has found a previous version of the Nebula client or tarball in the current working directory.")
    print("Please remove the current packages prior to initating.")
    exit()
#check for presence of previous installs
if os.path.exists(filename) == True:
    previousinstall()
if os.path.exists("*ebula") == True:
    previousinstall()
if os.path.exists("nebula-cert") == True:
    previousinstall()
if os.path.exists("config.yaml") == True:
    previousinstall()
#check system architecture for download logic
if platform.system() == "Darwin":
    download=(repo + nebversion + "/" + darwin)
if platform.system() == "Windows":
    download=(repo + nebversion + "/" + windows)
#some better architecture handling to be done here....
#testing shows platform.system() returns "linux" across ARM64 & AMD64
if platform.system() == "Linux":
    download=(repo + nebversion + "/" + amd64)
#download the Nebula tarball, correst for the host OS
urllib.request.urlretrieve(download, filename)
#check download came through
#ideally use hashlib here to grab the hash, record the hash and reference the hash when checking if DL succeeded
if os.path.exists(filename) != True:
    print("The download was unable to complete.")
    exit()
#unpack the downloaded tarfile
tf = tarfile.open(filename)
#extract the Nebula binary from the tarfile
tf.extractall()
#remove the original tarball and extra utilities
os.remove(filename)
#create nebula root CA
subprocess.run(["./nebula-cert", "ca", "-name", caname])
#check for CA creation and certificate presence
missingcert = "Certifiate is missing from working directory. Something has gone wrong!"
#check pubkey
if os.path.isfile('ca.crt'):
    path = os.getcwd()
    print("Nebula Certificate Location : " + path + "/" + "ca.crt")
else:
    print (missingcert)
    exit()
#check privkey
if os.path.isfile('ca.key'):
    path = os.getcwd()
    print("Nebula ED25519 Private Key Location : " + path + "/" + "ca.crt")
else:
    print (missingcert)
    exit()
