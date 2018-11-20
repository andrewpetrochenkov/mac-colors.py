[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/mac-colors.svg?longCache=True)](https://pypi.org/pypi/mac-colors/)
[![](https://img.shields.io/pypi/v/mac-colors.svg?maxAge=3600)](https://pypi.org/pypi/mac-colors/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-colors.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-colors.py/)

#### Install
```bash
$ [sudo] pip install mac-colors
```

#### Requirements
```bash
$ brew install tag
```

#### Functions
function|description
-|-
`mac_colors.blue(path)`|set blue tag
`mac_colors.get(path)`|return dictionary with path as key and tags as values
`mac_colors.gray(path)`|set gray tag
`mac_colors.green(path)`|set green tag
`mac_colors.grey(path)`|set grey tag
`mac_colors.none(path)`|remove all color tags
`mac_colors.orange(path)`|set orange tag
`mac_colors.purple(path)`|set purple tag
`mac_colors.red(path)`|set red tag
`mac_colors.replace(tags, path)`|replace tags
`mac_colors.yellow(path)`|set yellow tag

#### CLI
usage|description
-|-
`python -m mac_colors.blue path ...`|set blue tag
`python -m mac_colors.gray path ...`|set gray tag
`python -m mac_colors.green path ...`|set green tag
`python -m mac_colors.grey path ...`|set gray tag
`python -m mac_colors.none path ...`|remove all color tags
`python -m mac_colors.orange path ...`|set orange tag
`python -m mac_colors.purple path ...`|set purple tag
`python -m mac_colors.red path ...`|set red tag
`python -m mac_colors.yellow path ...`|set yellow tag

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

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>