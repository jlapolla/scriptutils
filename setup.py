# For general information, refer to:
# https://docs.python.org/3.6/distutils/index.html
# https://docs.python.org/3.6/distributing/index.html#distributing-index
# https://setuptools.readthedocs.io/en/latest/index.html
#
# For arguments to setup(), refer to:
# https://docs.python.org/3.6/distutils/apiref.html#distutils.core.setup
# https://setuptools.readthedocs.io/en/latest/setuptools.html#new-and-changed-setup-keywords


from setuptools import setup, find_packages


setup(
    name='jlapolla.scriptutils',
    version='0.1.0.dev1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['jlapolla'],
)
