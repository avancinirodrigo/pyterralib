from setuptools import setup  
from glob import glob
import os


setup(
    name = 'terralib',
    version = '5.5',
    author = 'TerraLib Team',
    author_email = 'terralib-team@terralib.org',
    description = ('A python binding for the TerraLib C++ library'),
    license = 'LGPL',
    keywords = 'terralib geo',
    url = 'http://dpi.inpe.br/terralib5',
    packages = ['terralib'],
    package_data = {'terralib': ['*.so*', '*.dll', '*.dylib', '*.pyd']},
    include_package_data=True
)