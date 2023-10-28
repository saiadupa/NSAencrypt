from setuptools import setup, find_packages

setup(
    name='ANSencrypt',
    version='1.0.0',
    author='Nithin sai Adupa',
    author_email='nithinsaiadupa@gmail.com',
    description='A package for encryption and decryption of images, video, text, and audio',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/saiadupa/ANSencrypt',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
