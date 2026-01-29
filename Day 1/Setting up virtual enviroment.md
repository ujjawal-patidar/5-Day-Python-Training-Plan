python3 -m venv .venv       -create and name the virtual enviroment
source .venv/bin/activate   - to activate the virtiual enviroment
deactivate                  - deactivate the VE

On Linux, you may have to install an additional package such as python3-pip

*You can make sure that pip is up-to-date by running:*
python3 -m pip install --upgrade pip
python3 -m pip --version

*To install packages*
python3 -m pip install <package_name>

pip searches the packages available in the open source pypi (python package index) - there are lots of packages developed by python community

*for specific version*
python3 -m pip install 'requests==2.18.4'

*to get latest 2.x release*
python3 -m pip install 'requests>=2.0.0,<3.0.0'

*for installing the extras of the package , extras are the dependencies or features which does not come by default*
python3 -m pip install 'requests[security]'







PEP 8 - Python Enhancement Proposals ,Style Guide for Python Code
class - Camal case with first letter capital
variable/function/method/ modules/packages - snake case, all small
constants - all upper case with snake case, just a convention , not constant actually
