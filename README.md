<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/mac-colors.svg?maxAge=3600)](https://pypi.org/project/mac-colors/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/mac-colors.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/mac-colors.py/actions)

### Installation
```bash
$ [sudo] pip install mac-colors
```

#### Requirements
```bash
$ brew install tag
```

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
    <a href="https://readme42.com/">readme42.com</a>
</p>
