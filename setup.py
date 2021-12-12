from setuptools import setup, find_packages

setup(
    name='xtrakt',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click', 'urlparse', 'sys', 'tldextract',
    ],
    entry_points={
        'console_scripts': [
            'xtrakt = xtrakt.main:cli',
        ],
    },
)