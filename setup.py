try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()


setup(
    name='py-morpheus',
    version='0.1',
    description='Toolkit for Linear algebra.',
    long_description=readme,
    author='Krishna Sangeeth KS',
    author_email='kskrishnasangeeth@gmail.com',
    url='https://github.com/whiletruelearn/morpheus',
    keywords='linear algebra toolkit',
    packages=['whatthelang'],
    include_package_data=True,
    license=license,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)