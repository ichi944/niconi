niconi
======

sublime text 3 plugin for simple replacing by clipboard between html tags like '>' and '&lt;'

this plugin help you html editing by copy and paste

install
-------

#### on mac

copy niconi directory under `~/Library/Application Support/Sublime Text 3/Packages`

#### short cut key

edit this file

example: set "alt + command + v"

`~/Library/Application Support/Sublime Text 3/Packages/User/Default (OSX).sublime-keymap`

    [
      {"keys": ["alt+super+v"], "command": "niconi"}
    ]

usage
-----

there is

`<p>yazawa</p>`

you put cursor between tags and then you run shortcut-key or
show console and run
`view.run_command('niconi')`

and then

`<p>[your clipboard string]</p>`

