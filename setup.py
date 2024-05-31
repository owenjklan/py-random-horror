import setuptools

setuptools.setup(
    name="random_horror",
    version="0.0.1",
    url="https://github.com/owenjklan/py-random-horror",
    author="Owen Klan",
    author_email="private@example.com",
    description="'Random Horror' generation, as an installable python package.",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    install_requires=['importlib_resources'],
)