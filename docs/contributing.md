## Install for development

```
git clone ... && cd ...
virtualenv .env --python /usr/bin/python3
python setup.py develop
```


## Tests

You can run the old-school `setup.py test` or simply `tox`.


#### Lint the project

```
tox -e lint
```

Strive to keep the score 9.5 or higher.


## Recommended workflow

#### before push

  - `tox`
  - `tox -e lint`
  - PyCharm's fix (Code -> Reformat Code -> Scope: Project Files) and check (Code -> Inspect Code -> Whole project)


#### on new version release

  - `git checkout master && git merge ...`
  - add commit with these changes:
      - bump version
      - add changelog entry
      - `git tag -a v0.X.Y -m 'short description'`
  - the same as 'before push'
  - `git push origin master --tags`
  - check all the CI tests and coverage
  - `TWINE_USERNAME=MY_NAME python setup.py upload`
