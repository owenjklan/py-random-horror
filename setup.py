import setuptools

setuptools.setup(
    name="random_horror_gen",
    version="0.0.3",
    url="https://github.com/owenjklan/py-random-horror",
    author="Owen Klan",
    author_email="private@example.com",
    description="'Random Horror' generation, as an installable python package.",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    install_requires=['importlib_resources'],
    install_package_data=True,
    package_data={'random_horror_gen': ['lists/*']},
)
