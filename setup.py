from setuptools import setup, find_packages
import os
import sys
import shutil

if os.path.exists('/home/xilinx/test'):
   shutil.rmtree('/home/xilinx/test')
shutil.copytree('test','/home/xilinx/test')
print("Done downloading test from git!")
setup(
   name = "test",
   version = '1.0',
   url = 'https://github.com/adriankaisinclair/test',
   license = 'All right',
   author = "Adrian Sinclair",
   author_email = "aksincla@asu.edu",
   packages = [],
   package_data = {
   '' : ['*.txt','*.md'],
   },
   description = "test"
)
