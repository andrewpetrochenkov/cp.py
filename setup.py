import setuptools

setuptools.setup(
    name='cp',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
