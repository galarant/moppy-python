__author__ = "jeff.revesz@buzzfeed.com (Jeff Revesz)"

try:
    from setuptools import setup, find_packages
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='moppy-python',
    version='0.0.1',
    packages=find_packages(),
    author='Jeff Revesz',
    author_email='jeff.revesz@buzzfeed.com',
    description='A rebuild of the Moppy project in Python',
    test_suite='nose.collector',
    url='http://github.com/galarant/moppy-python',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
    ],
    keywords="serial floppy arduino music",

)
