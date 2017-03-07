#!/bin/bash

# ensure necessary libraries are installed
sudo apt-get install python3-pip
sudo -H pip3 install twine
sudo -H pip3 install sphinx

# generate package information
python3 setup.py egg_info

# generate documentation
mkdir html
sphinx-build docs html
cd html/;zip -r ../docu.zip *; cd ..

echo "Upload PKG-INFO and docu.zip to pypi"

# upload source code
python setup.py sdist
twine upload dist/pyjulius3-0.4.tar.gz
