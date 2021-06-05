# How It Works
Once you have the travis command - line tool installed, from the root of your project do:

travis encrypt --add deploy.password
This will encrypt your locally-stored PyPI password and save that to your .travis.yml file. Commit that change to git.

# Build locally and check documentation:

python3 -m pip install --user --upgrade build
python3 -m build
pip3 install -U twine
twine check dist/*

# Your Release Process
If you are using this feature, this is how you would do a patch release:

pip3 install -r requirements_dev.txt

bump2version patch
git push --tags