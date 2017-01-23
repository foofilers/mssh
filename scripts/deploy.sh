 #!/bin/sh

 python3 setup.py clean sdist bdist_wheel
 twine register dist/*
 twine upload dist/*