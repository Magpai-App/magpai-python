from distutils.core import setup
from magpai.version import Version


setup(name='magpai',
    version=Version('1.0.1').number,
    description='Magpai python bindings',
    long_description=open('README.md').read().strip(),
    author='Package Author',
    author_email='ben@magpai.app',
    url='http://magpai.app',
    py_modules=['magpai'],
    install_requires=[],
    license='MIT License',
    zip_safe=False,
    keywords='magpai ai workflows',
    classifiers=['Packages', 'Boilerplate'])