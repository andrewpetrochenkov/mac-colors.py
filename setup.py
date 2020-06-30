import setuptools

setuptools.setup(
    name='mac-colors',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
