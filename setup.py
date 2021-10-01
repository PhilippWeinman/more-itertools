from re import sub

from setuptools import setup, find_packages


def get_long_description():
    # Fix display issues on PyPI caused by RST markup
    readme = open('README.rst').read()

    version_lines = []
    with open('docs/versions.rst') as infile:
        next(infile)
        for line in infile:
            line = line.rstrip().replace('.. automodule:: more_itertools', '')
            version_lines.append(line)
    version_history = '\n'.join(version_lines)
    version_history = sub(r':func:`([a-zA-Z0-9._]+)`', r'\1', version_history)

    ret = readme + '\n\n' + version_history
    return ret


setup(
    name='more-itertools',
    version='6.1.0',
    description='More routines for operating on iterables, beyond itertools',
    long_description=get_long_description(),
    author='Erik Rose',
    author_email='erikrose@grinchcentral.com',
    license='MIT',
    packages=find_packages(exclude=['ez_setup']),
    python_requires='>=3.4',
    test_suite='more_itertools.tests',
    url='https://github.com/erikrose/more-itertools',
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries'],
    keywords=['itertools', 'iterator', 'iteration', 'filter', 'peek',
              'peekable', 'collate', 'chunk', 'chunked'],
)
