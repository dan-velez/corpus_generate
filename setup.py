from setuptools import setup, find_packages

setup(name='corpus_generate',
    version='0.0.1',
    description='Use the net to generate training data for a text classifier.',
    url='https://github.com/dan-velez/corpus_generate',
    author='Daniel Velez',
    author_email='daniel.enr.velez@gmail.com',
    license='MIT',
    python_requires=">=3.6",
    packages=['corpus_generate'],
    entry_points={
        'console_scripts': ['corpus-generate=corpus_generate.__main__:main']
    },
    install_requires=['requests_html==0.10.0',
                      'beautifulsoup4==4.8.0',
                      'newspaper3k==0.2.8',
                      'nltk==3.4.5',
                      'google==3.0.0'])