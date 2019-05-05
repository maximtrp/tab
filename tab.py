#!/usr/bin/python
import os
import yaml
from functools import reduce
from optparse import OptionParser


# Command-line options
parser = OptionParser(usage="Usage: %prog [options]")
parser.add_option("-c", dest="columns_num", type="int", metavar='NUM', help='maximum columns number', default=6)
parser.add_option("-s", "--css", dest="styles", action="store_true", help='integrate "template/styles.css" into index.html', default=False)
parser.add_option("-r", dest="remove_icons", action="store_true", help="remove icons", default=False)
options, args = parser.parse_args()

def iconify(icon_name):
    return '<i class="' + icon_name + ' icon"></i>'

if not options.remove_icons:
    icons = {'group': 'folder open', 'entry': 'linkify'}

if options.styles:
    f = open('template/styles.css', 'r')
    styles = f.read()
    f.close()

# Importing bookmarks
bm = open('bookmarks.yml')
bm_yaml = yaml.safe_load(bm)
bm.close()


# Importing template files
with open('template/index.html') as f:
    body_tmp = f.read()
with open('template/group.html') as f:
    group_tmp = f.read()
with open('template/link.html') as f:
    link_tmp = f.read()


# Iterating YAML
# bm_yaml is a list of dicts
groups_prehtml = []

for group_title, entries in bm_yaml.items():
    # Group contains title and entries
    # Iterating a group
    entries_prehtml = []
    # Iterating over entries and attributes
    for entry_title, entry_info in entries.items():
        # Icons
        if not options.remove_icons:
            icon = icons['entry'] if 'icon' not in entry_info else entry_info['icon']
            entry_title = iconify(icon) + entry_title

        # Links HTML
        rep = ('{title}', entry_title), ('{href}', entry_info['href'])
        entry_str = reduce(lambda a, k: a.replace(*k), rep, link_tmp.strip())
        entries_prehtml.append(entry_str)

    # Combining entries HTMLs
    entries_html = " ".join(entries_prehtml)
    if not options.remove_icons:
        group_title = iconify(icons['group']) + group_title

    # Group HTML
    rep = ('{groupname}', group_title), ('{links}', entries_html)
    group_str = reduce(lambda a, v: a.replace(*v), rep, group_tmp)
    groups_prehtml.append(group_str)


# Combining groups
group_html = "\n".join(groups_prehtml)
num_words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}
num = min(len(bm_yaml), options.columns_num)
rep = ('{groups}', group_html), ('{num}', num_words[num]),\
        ('{styles}', styles if options.styles else ''),\
        ('{styles_ext}', '' if options.styles else '<link rel="stylesheet" type="text/css" href="styles.css">')
body_html = reduce(lambda a, v: a.replace(*v), rep, body_tmp)


# Creating an output dir
os.makedirs('output', exist_ok=True)


# Writing a file
f = open('output/index.html', 'w')
f.write(body_html)
f.close()
