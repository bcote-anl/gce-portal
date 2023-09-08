import os
from setuptools import setup, find_packages

version_ns = {}
with open(os.path.join('gce_portal', 'version.py')) as f:
    exec(f.read(), version_ns)
version = version_ns['__version__']

install_requires = []
with open('requirements.txt') as reqs:
    for line in reqs.readlines():
        req = line.strip()
        if not req or req.startswith('#'):
            continue
        install_requires.append(req)


setup(
    name='gce_portal',
    description='A portal for galactic chemical evolution (GCE) data generated by interactive data services.',
    url='https://github.com/bcote-anl/gce-portal',
    maintainer='Benoit Cote',
    maintainer_email='',
    version=version,
    packages=find_packages(),
    install_requires=install_requires,
    dependency_links=[],
    license='Apache 2.0',
    classifiers=[]
)
