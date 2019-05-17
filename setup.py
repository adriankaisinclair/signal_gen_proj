from setuptools import setup, find_packages
import os
import sys
import shutil

py_dir = "/usr/local/lib/python3.6/dist-packages/signal_gen"
nb_dir = "/home/xilinx/jupyter_notebooks/signal_gen.ipynb"

#place signal_gen.ipynb at ~/jupyter_notebooks
if os.path.exists(nb_dir):
   os.remove(nb_dir)
shutil.move("signal_gen.ipynb",nb_dir)

#place folder signal_gen at py_dir 
if os.path.exists(py_dir):
   shutil.rmtree(py_dir)
shutil.copytree('signal_gen',py_dir)

print("Done downloading signal_gen_proj from git!")
setup(
   name = "signal_gen_proj",
   version = '1.0',
   url = 'https://github.com/adriankaisinclair/signal_gen_proj',
   license = 'BSD 3',
   author = "Adrian Sinclair",
   author_email = "aksincla@asu.edu",
   packages = [],
   package_data = {
   '' : ['*.txt','*.md','*.ipynb'],
   },
   description = "signal_gen_proj"
)
