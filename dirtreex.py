#!/usr/bin/env python
import argparse
import os

from walkdir import filtered_walk

parser = argparse.ArgumentParser(description='Print the directory-tree code for the LaTeX dirtree package.')
parser.add_argument(dest='path', type=str, help="Root directory of the tree")
parser.add_argument('-d', '--maxDepth', dest='maxDepth', type=int, help="Max depth for tree expansion")
parser.add_argument('-H', '--includeHidden', dest='includeHidden', action='store_true', help='Include hidden files')
parser.add_argument('-S', '--includeSystem', dest='includeSystem', action='store_true', help='Include system files')

system_file_names = [".DS_Store"]


# Delete trailing / in rootDir which can lead to errors
def delete_trailing_slash(path_name):
    while path_name.endswith('/'):
        path_name = path_name[:-1]
    return path_name


# Count how many levels deep is the directory with respect to dirRoot
def get_relative_depth(dir_path, level_offset):
    return dir_path.count(os.path.sep) - level_offset


# Escape illegal symbols for LaTeX
def escape_illegal(name):
    illegal_char_array = ['\\', '&', '%', '$', '#', '_', '{', '}', '~', '^']
    for char in illegal_char_array:
        name = name.replace(char, "\\" + char)
    return name


rootDir = delete_trailing_slash(parser.parse_args().path)
includeHidden = parser.parse_args().includeHidden
includeSystem = parser.parse_args().includeSystem
maxDepth = parser.parse_args().maxDepth

# if the directory exists
if os.path.isdir(rootDir) and os.path.exists(rootDir):

    indentChar = " "

    # Depth of the root (i.e. number of "/")
    levelOffset = rootDir.count(os.path.sep) - 1

    # Create filter
    excluded_filter = []
    if not includeHidden:
        excluded_filter.append(".*")
    if not includeSystem:
        excluded_filter += system_file_names

    print ("\dirtree{%")
    for dirName, subdirList, fileList in sorted(filtered_walk(rootDir, depth=maxDepth, excluded_dirs=excluded_filter,
                                                       excluded_files=excluded_filter)):

        level = get_relative_depth(dirName, levelOffset)

        baseName = os.path.basename(dirName)

        if level == 1:  # for the first level only print the whole path
            print(indentChar + "." + str(level) + " {" + escape_illegal(dirName) + "} .")
        else:
            print(indentChar * level + "." + str(level) + " {" + escape_illegal((os.path.basename(dirName))) + "} .")

        level += 1
        for fileName in sorted(fileList):
            print(indentChar * level + "." + str(level) + " {" + escape_illegal(fileName) + "} .")
    print ("}")
else:
    print ("Error: root directory not found")


#https://raw.githubusercontent.com/mauriziodimatteo/dirtreex/master/dirtreex.py

#Help on function filtered_walk in module walkdir:
#
#filtered_walk(top, included_files=None, included_dirs=None, excluded_files=None, excluded_dirs=None, depth=None, followlinks=False, min_depth=None)
#    This is a wrapper around ``os.walk()`` and other filesystem traversal
#    iterators, with these additional features:
#
#     - *top* may be either a string (which will be passed to ``os.walk()``)
#       or any iterable that produces sequences with ``path, subdirs, files``
#       as the first three elements in the sequence
#     - allows independent glob-style filters for filenames and subdirectories
#     - allows a recursion depth limit to be specified
#     - allows a minimum depth to be specified to report only subdirectory
#       contents
#     - emits a message to stderr and skips the directory if a symlink loop
#       is encountered when following links
#
#    Filtered walks created by passing in a string are always top down, as
#    the subdirectory listings must be altered to provide a number of the
#    above features.
#
#    *include_files*, *include_dirs*, *exclude_files* and *exclude_dirs* are
#    used to apply the relevant filtering steps to the walk.
#
#    A *depth* of ``None`` (the default) disables depth limiting. Otherwise,
#    *depth* must be at least zero and indicates how far to descend into the
#    directory hierarchy. A depth of zero is useful to get separate filtered
#    subdirectory and file listings for *top*.
#
#    Setting *min_depth* allows directories higher in the tree to be
#    excluded from the walk (e.g. a *min_depth* of 1 excludes *top*, but
#    any subdirectories will still be processed)
#
#    *followlinks* enables symbolic loop detection (when set to ``True``)
#    and is also passed to ``os.walk()`` when top is a string
#(END)