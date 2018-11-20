#!/usr/bin/env python
"""set red tag"""
import os
import click
import mac_colors


MODULE_NAME = "mac_colors.%s" % os.path.splitext(os.path.basename(__file__))[0]
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = "python -m %s path ..." % MODULE_NAME


@click.command()
@click.argument('path', nargs=-1, required=True)
def _cli(path):
    mac_colors.red(path)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
