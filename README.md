# PIP-package-creation
created PIP package  for the sum of N natural numbers using setup tools

create a base folder, go inside that and create a package folder
Go inside package folder and create .py(NnaturalNumbers.py) file to compute sum of n natural numbers
In the same package folder create __init__.py file and write from NnaturalNumbers(.py file name) import (function name) NnaturalSum and save it.
Go back to the base folder,create setup.py file to add description of package and supporting OS etc.
Folder structure:
  Base_folder:
           1. Package folder(SumNnumbers)
                                   1. NnaturalNumbers.py
                                   2. __init.py
           2. setup.py
Got to commanda prompt:
Run the below commands to create a package:

1.pip3 install setptools
2.python setup.py bdist sdist_wheel(creating a package)

if second command throws any error then try running this

pip install wheel

Generally if package is created successfully you can see the different folders created in the base folder sucha sa dist,build folder
 If you want to upload any package in pypi.org create an account and install twine using pip install twine
 then use the below command to upload and give your credentials
        twine upload dist/*


