# install some libraries here, e.g. `sudo apt-get install libbz2-dev`

pyenv install 3.9.9
pyenv virtualenv 3.9.9 my-new-project-name

pip install -r requirements.txt
python setup.py develop

# run some other initialization steps here
