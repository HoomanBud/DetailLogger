from setuptools import setup, find_packages

setup(
    name='detaillogger',
    version='0.0.6',
    description='Simple detail logger for webservers',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    license='MIT',
    packages=find_packages(),
    author='Hooman Bud',
    author_email='hoomanbud5511@gmail.com',
    url='https://github.com/HoomanBud/DetailLogger',
)