# tab

`tab` is a simple start page generator written in Python. It uses primitive templating, YAML, and outputs a single `index.html`. Default template is based on [Semantic UI](https://semantic-ui.com/).

## Basics

Bookmarks are stored in a separate YAML file named `bookmarks.yml`. Its format should fit the following one:

```yml
Coding:
    GitHub:
        href: //github.com
        icon: git
    Travis CI:
        href: //travis-ci.org
    BitBucket:
        href: //bitbucket.org
        icon: bitbucket

Learn:
    Stepik:
        href: //stepik.org
    Udacity:
        href: //udacity.com
    KhanAcademy:
        href: //khanacademy.org
```

This format is simple and intuitive. `Coding` is a group name (non-indeted block), `GitHub` is an entry (link) name, `href` is used to store an URL (`tab` does not process it in any way now, so it is up to you), `icon` is an icon name (see full list at [Semantic UI](https://semantic-ui.com/elements/icon.html)).

Template files are currently hardcoded to be placed in a `template` dir. There must be `index.html`, `group.html`, `link.html` files.

Stylesheet `styles.css` is optional. It may be integrated into `index.html`(use `-s` flag).

By default, group and link icons are enabled. To disable, use `-r` flag. You may specify maximum columns number with `-c` flag.

## Template

You may create your own template. Just be sure to use these template variables:

* `{styles}` is for an integrated stylesheet.
* `{styles_ext}` is for an external stylesheet.
* `{groups}` — wrapper placeholder for all groups html.
* `{groupname}` — name of a group.
* `{links}` — placeholder for links.
* `{title}` — link title.
* `{href}` — link href.

## Usage

Run with a `-h` flag to see help.

```bash
$ python tab.py -h
Usage: tab.py [options]

Options:
  -h, --help  show this help message and exit
  -c NUM      maximum columns number
  -s, --css   integrate "template/styles.css" into index.html
  -r          remove icons
```

## Example

There is an example `index.html` in `output` dir.

![Screenshot](https://raw.githubusercontent.com/maximtrp/tab/master/images/screenshot.png "Screenshot")
