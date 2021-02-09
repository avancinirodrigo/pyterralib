from distutils.core import setup  

setup(
    name = 'terralib',
    version = '@TERRALIB_VERSION_STRING@',
    author = 'TerraLib Team',
    author_email = 'terralib-team@terralib.org',
    description = ('A python binding for the TerraLib C++ library'),
    license = 'LGPL',
    keywords = 'terralib geo',
    url = 'http://dpi.inpe.br/terralib5',
    packages=['terralib'],
    package_data={'terralib':['*.so*', '*.dll', '*.dylib', '*.pyd']}
)