.. PyPI| |PyPI - Python Version| |PyPI - Implementation|

|Build Status| |Coverage Status|

Blank Python Project
====================

Here I have collected all the stuff that I need in order to create an open-source python package:


Features
--------

- stable folders structure (`<docs/>`_, `src/ <pyblank/>`_, `<tests/>`_)
- `<LICENSE>`_ included
- PyCharm support (predefined inspection settings, styles, etc) (`<.idea/>`_)
- distribution with setuptools (`<setup.py>`_, `<MANIFEST.in>`_) and pip (`<requirements.txt>`_)
- testing support via ``tox`` (`<tests/>`_, `<tox.ini>`_)
- GitLab CI (via `<.gitlab-ci.yml>`_) and Travis CI (via `<.travis.yml>`_) support
- support tests and CI with PyPy
- `CHANGELOG <CHANGELOG.md>`_, `TODO <TODO.md>`_ and `README <README.rst>`_ for documentation
- versioning support (`<pyblank/__version__.py>`_)
- gitignore rules for Python (`<.gitignore>`_)


Structure
---------

The structure is as follows:

.. code-block:: text

    ├── .idea/                              # PyCharm project settings (can be safely removed)
    │   ├── codeStyles/                     # custom code styles
    │   │   ├── codeStyleConfig.xml
    │   │   └── Project.xml                 # use custom line length=100
    │   ├── codeStyleSettings.xml           # old format for custom styles (before v2017.3)
    │   ├── dictionaries/                   # save any words here to prevent marking them as typo
    │   │   ├── .gitignore                  # (you have to restart PyCharm and rerun Code -> Inspect Code)
    │   │   ├── default.xml                 # for all projects
    │   │   └── project.xml                 # for this project only
    │   ├── inspectionProfiles/
    │   │   └── Project_Default.xml         # enable custom code inspections for the project
    │   ├── modules.xml
    │   ├── pyblank.iml                     # the main project file
    │   └── vcs.xml
    ├── docs/                               # put your docs here
    │   └── contributing.md
    ├── pyblank/                            # sources
    │   ├── __init__.py
    │   ├── __version__.py
    │   ├── config.py
    │   ├── log.py
    │   └── utils.py
    ├── tests
    │   ├── __init__.py
    │   └── test.py
    ├── .fix.sh                             # shell script for fixing tabs, empty spaces, etc
    ├── .gitignore
    ├── .gitlab-ci.yml                      # hosting on Gitlab? https://docs.gitlab.com/ee/ci/
    ├── .travis.yml                         # hosting on Github? https://github.com/marketplace/travis-ci
    ├── CHANGELOG.md                        # write any changes between versions
    ├── LICENSE                             # MIT License is the most basic
    ├── MANIFEST.in                         # https://docs.python.org/3/distutils/sourcedist.html#specifying-the-files-to-distribute
    ├── README.rst                          # this file; standard way to provide long description
    ├── requirements.txt                    # package dependencies
    ├── setup.py                            # standard distribution script
    ├── TODO.md                             # what to do next with your package?
    └── tox.ini                             # run style and unit tests


Usage
-----

.. code-block::

    PROJ=awesome
    git clone https://github.com/tsionyx/pyblank.git $PROJ && cd $PROJ
    rm -rf .git

    mv pyblank/ $PROJ/
    mv .idea/pyblank.iml .idea/${PROJ}.iml
    for f in .idea/${PROJ}.iml .idea/modules.xml .idea/dictionaries/project.xml .gitlab-ci.yml .travis.yml setup.py tests/test_example.py; do
        sed "s/pyblank/$PROJ/g" -i ${f}
    done

    echo -e "$PROJ\n=====" > README.rst
    sed "s/1970-01-01/$(date +'%Y-%m-%d')/" -i CHANGELOG.md

    # fill in the project metadata
    vim setup.py

    git init
    git add .
    git commit -m 'initial commit'
    git tag -a v0.0.1 -m 'initial project structure'

    pycharm.sh .


.. |Build Status| image:: https://img.shields.io/travis/tsionyx/pyblank.svg
    :target: https://travis-ci.org/tsionyx/pyblank
.. |Coverage Status| image:: https://img.shields.io/coveralls/github/tsionyx/pyblank.svg
    :target: https://coveralls.io/github/tsionyx/pyblank
.. |PyPI| image:: https://img.shields.io/pypi/v/pyblank.svg
    :target: https://pypi.org/project/pyblank/
.. |PyPI - Python Version| image:: https://img.shields.io/pypi/pyversions/pyblank.svg
    :target: https://pypi.org/project/pyblank/
.. |PyPI - Implementation| image:: https://img.shields.io/pypi/implementation/pyblank.svg
    :target: https://pypi.org/project/pyblank/
