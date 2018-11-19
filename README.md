[![](https://img.shields.io/pypi/pyversions/cp.svg?longCache=True)](https://pypi.org/pypi/cp/)
[![](https://img.shields.io/pypi/v/cp.svg?maxAge=3600)](https://pypi.org/pypi/cp/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/cp.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/cp.py/)

#### Install
```bash
$ [sudo] pip install cp
```

#### Functions
function|description
-|-
`cp.cp(source, target, force=True)`|Copy the directory/file src to the directory/file target

#### Examples
```python
>>> import cp

>>> cp.cp(src,dst)
>>> cp.cp(src,dst) # skip, exists
>>> cp.cp(src,dst,force=True) # force cp
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>