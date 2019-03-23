#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import public
import runcmd
import values

"""
https://github.com/jdberry/tag
"""

bin = "/usr/local/bin/tag"


def _run(args):
    if not os.path.exists("/usr/local/bin/tag"):
        raise OSError("""/usr/local/bin/tag NOT INSTALLED

https://github.com/jdberry/tag
brew install tag
""")
    args = ["/usr/local/bin/tag"] + list(args)
    return runcmd.run(args)._raise().out


@public.add
def add(tags, path):
    """add tags"""
    if tags:
        args = ["-a", ",".join(tags)] + list(set(values.get(path)))
        _run(args)


@public.add
def replace(tags, path):
    """replace tags"""
    if tags:
        args = ["-s", ",".join(tags)] + list(set(values.get(path)))
        _run(args)


@public.add
def none(path):
    """remove all color tags"""
    args = ["-r", "*"] + list(set(values.get(path)))
    _run(args)


@public.add
def rm(tags, path):
    """remove tags"""
    paths = list(set(values.get(path)))
    if tags and path:
        args = ["-r", ",".join(tags)] + paths
        _run(args)


@public.add
def blue(path):
    """set blue tag"""
    replace(["blue"], path)


@public.add
def gray(path):
    """set gray tag"""
    replace(["gray"], path)


@public.add
def grey(path):
    """set grey tag"""
    replace(["gray"], path)


@public.add
def green(path):
    """set green tag"""
    replace(["green"], path)


@public.add
def orange(path):
    """set orange tag"""
    replace(["orange"], path)


@public.add
def purple(path):
    """set purple tag"""
    replace(["purple"], path)


@public.add
def red(path):
    """set red tag"""
    replace(["red"], path)


@public.add
def yellow(path):
    """set yellow tag"""
    replace(["yellow"], path)


@public.add
def get(path):
    """return dictionary with path as key and tags as values"""
    args = ["-l"] + list(set(values.get(path)))
    out = _run(args)
    result = dict()
    for l in out.splitlines():
        if "\t" in l:
            path, tags = l.split("\t")
            result[path] = tags.split(",")
        else:
            result[l] = []
    return result
