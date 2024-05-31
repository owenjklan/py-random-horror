## What is this package?
This package provides the base functionality of the "Random Horror"
generator, but now in the form of a Python package,
intended to be installed using `pip` and the
git repository URL.

Ultimately, this is for a personal portfolio project that I have
in the works.

More to come.

### To install with `pip`
Use a command similar to the following to install:
```shell
pip3 install --user git+https://github.com/owenjklan/py-random-horror.git
```

If you need to upgrade to a newer version:
```shell
pip3 install --upgrade --user git+https://github.com/owenjklan/py-random-horror.git
```

#### IMPORTANT REMINDER!
If changes are made to the code in the repository, then the `version`
value inside of `setup.py` will need to be bumped. Otherwise,
`pip3 install --upgrade` won't see anything that it believes it
needs to update.