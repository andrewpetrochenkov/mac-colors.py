#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mac_colors

path = [__file__]
mac_colors.purple(path)
for path, colors in mac_colors.get(path).items():
    print("%s: %s" % (path, colors))
