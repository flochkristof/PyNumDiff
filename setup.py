import os
from setuptools import setup, find_packages
PACKAGES = find_packages()

# Get version and release info, which is all stored in pynumdiff/__version__.py
ver_file = os.path.join('pynumdiff', '__version__.py')
with open(ver_file) as f:
    exec(f.read())

opts = dict(name=NAME,
            maintainer="Floris van Breugel, Yuying Liu",
            maintainer_email="fvanbreugel@unr.edu, yliu814@uw.edu",
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            url=URL,
            download_url=DOWNLOAD_URL,
            license=LICENSE,
            classifiers=CLASSIFIERS,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            platforms=PLATFORMS,
            version=VERSION,
            packages=PACKAGES,
            package_data=PACKAGE_DATA,
            install_requires=REQUIRES,
            requires=REQUIRES)


if __name__ == '__main__':
    setup(**opts)
