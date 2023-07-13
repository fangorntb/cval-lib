rm -r sdist
python setup.py sdist
twine upload dist/*

