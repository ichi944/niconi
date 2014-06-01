niconi
======

sublime text 3 plugin for simple replacing by clipboard between html tags like '>' and '&lt;'

this plugin help you html editing by copy and paste

install
-------

#### on mac

clone or download

and copy Niconi directory under `~/Library/Application Support/Sublime Text 3/Packages`

#### short cut key

example: set "alt + command + v"

edit this file if file not exists, create this

`~/Library/Application Support/Sublime Text 3/Packages/User/Default (OSX).sublime-keymap`

add setteing

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

