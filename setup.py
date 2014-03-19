from distutils.core import setup

setup(
    name='JcvUtils',
    version='0.1.0',
    author='Junior Vidotti',
    author_email='jrvidotti@gmail.com',
    packages=['jcvutils', 'jcvutils.features'],
    scripts=[],
    url='http://pypi.python.org/pypi/JCVUtils/',
    license='LICENSE.txt',
    description='My utils: phone formatting, CPF/CGC checking, etc.',
    long_description=open('README.txt').read(),
    install_requires=[
        "argparse >= 1.2.1",
        "fuzzywuzzy >= 0.2",
        "lettuce >= 0.2.19",
        "sure >= 1.2.3",
        "wsgiref >= 0.1.0"
    ],
)


