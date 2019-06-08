<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/mac-colors.svg?longCache=True)](https://pypi.org/project/mac-colors/)
[![](https://img.shields.io/pypi/v/mac-colors.svg?maxAge=3600)](https://pypi.org/project/mac-colors/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-colors.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-colors.py/)

#### Installation
```bash
$ [sudo] pip install mac-colors
```

#### Requirements
```bash
$ brew install tag
```

#### Functions
function|`__doc__`
-|-
`mac_colors.add(tags, path)` |add tags
`mac_colors.get(path)` |return dictionary with path as key and tags as values
`mac_colors.replace(tags, path)` |replace tags
`mac_colors.rm(tags, path)` |remove tags

#### Executable modules
usage|`__doc__`
-|-
`python -m mac_colors.blue path ...` |set blue tag
`python -m mac_colors.gray path ...` |set gray tag
`python -m mac_colors.green path ...` |set green tag
`python -m mac_colors.grey path ...` |set gray tag
`python -m mac_colors.none path ...` |remove all color tags
`python -m mac_colors.orange path ...` |set orange tag
`python -m mac_colors.purple path ...` |set purple tag
`python -m mac_colors.red path ...` |set red tag
`python -m mac_colors.yellow path ...` |set yellow tag

#### Examples
```python
>>> import mac_colors
>>> path = ["path/to/file"]
>>> mac_colors.red(path)
```
get
```python
>>> mac_colors.get(path)
{'path/to/file':["red"]}
```
set multiple colors
```python
>>> mac_colors.replace(["blue","red"],path)
```
remove colors
```python
>>> mac_colors.none(path)
```

#### Links
+   [tag](https://github.com/jdberry/tag)

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>